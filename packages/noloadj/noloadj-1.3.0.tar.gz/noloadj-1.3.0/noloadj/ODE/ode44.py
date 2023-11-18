import jax.numpy as np
from jax.lax import *
from jax import custom_jvp,jvp
from functools import partial

def odeint44(f,x0,vect_t,*P):
    return _odeint44(f,x0,vect_t,*P)


def rk_step(x_prev, t_prev, h,f,*P):
    k1 = f.derivative(x_prev, t_prev,*P)
    k2 = f.derivative(x_prev + h*0.5 * k1, t_prev + 0.5 * h,*P)
    k3 = f.derivative(x_prev + h*0.5 * k2, t_prev + 0.5 * h,*P)
    k4 = f.derivative(x_prev + h*k3, t_prev + h,*P)

    x_now = x_prev + h *(k1 + 2 * k2 + 2 * k3 + k4) / 6
    t_now = t_prev + h
    return x_now,t_now


def next_step_simulation(x_prev,t_prev,h,f,*P):
    x_now,t_now=rk_step(x_prev,t_prev,h,f,*P)
    y_now=f.output(x_now,t_now,*P)
    return x_now,t_now,y_now

@partial(custom_jvp,nondiff_argnums=(0,))
def _odeint44(f,x0,vect_t,*P):
    h=vect_t[1]-vect_t[0]

    def scan_fun(state,te):

        x_prev,t_prev,y_prev=state

        x_now,t_now,y_now=next_step_simulation(x_prev,t_prev,h,f,*P)

        return (x_now,t_now,y_now),(x_now,y_now)


    y0=f.output(x0,0.,*P)
    vect,(xf,yf)=scan(scan_fun,(x0,vect_t[0],y0),vect_t[1:])

    xf=np.transpose(np.concatenate((x0[None], xf)))
    yf=np.transpose(np.concatenate((y0[None], yf)))

    return xf,yf


@_odeint44.defjvp
def _odeint44_jvp(f, primals, tangents):
    x0, vect_t, *P = primals
    dx0, _, *dP = tangents
    nPdP = len(P)

    xf,dxf,yf,dyf = odeint44_etendu(f,nPdP,x0,dx0,vect_t,*P,*dP)
    return (xf,yf),(dxf,dyf)

def f_grads(x,dx, t, f,nPdP,*P_and_dP):
    P, dP = P_and_dP[:nPdP], P_and_dP[nPdP:]
    res, dres = jvp(f.derivative, (x, t, *P), (dx, 0., *dP))
    return dres

def rk44_step_der(x_prev, t_prev, dx_prev,h,f,nPdP,*P_and_dP):
    P,_ = P_and_dP[:nPdP],P_and_dP[nPdP:]
    k1 = f.derivative(x_prev, t_prev,*P)
    k2 = f.derivative(x_prev + h*0.5 * k1, t_prev + 0.5 * h,*P)
    k3 = f.derivative(x_prev + h*0.5 * k2, t_prev + 0.5 * h,*P)
    k4 = f.derivative(x_prev + h*k3, t_prev + h,*P)

    dk1 = f_grads(x_prev, dx_prev, t_prev,f,nPdP, *P_and_dP)
    dk2 = f_grads(x_prev + h*0.5 * k1, dx_prev + h * 0.5 * dk1,t_prev +
                0.5 * h,f,nPdP,*P_and_dP)
    dk3 = f_grads(x_prev + h*0.5 * k2, dx_prev + h * 0.5 * dk2,t_prev +
                0.5 * h,f,nPdP,*P_and_dP)
    dk4 = f_grads(x_prev + h * k3,dx_prev + h * dk3,t_prev+h,f,nPdP,*P_and_dP)

    x_now = x_prev + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    dx_now = dx_prev + h *(dk1 + 2 * dk2 + 2 * dk3 + dk4) / 6
    return dx_now,x_now

def next_der_step_simulation(x_prev,t_prev,dx_prev,h,f,
                             nPdP,*P_and_dP):
    P,dP = P_and_dP[:nPdP],P_and_dP[nPdP:]
    dx_now,x_now = rk44_step_der(x_prev, t_prev, dx_prev,h,f,nPdP,
                              *P_and_dP)
    t_now=t_prev+h
    y_now=f.output(x_now,t_now,*P)
    dy_now = jvp(f.output, (x_now, t_now, *P), (dx_now, 0., *dP))[1]
    return dx_now,dy_now,x_now,y_now,t_now

def odeint44_etendu(f,nPdP,x0,dx0,vect_t,*P_and_dP):
    P,dP = P_and_dP[:nPdP],P_and_dP[nPdP:]
    h=vect_t[1]-vect_t[0]

    def scan_fun(state, te):

        x_prev,dx_prev,y_prev,dy_prev,t_prev=state

        dx_now,dy_now,x_now,y_now,t_now=next_der_step_simulation(x_prev,t_prev,
                            dx_prev, h,f,nPdP,*P_and_dP)

        return (x_now,dx_now,y_now,dy_now,t_now), (x_now,dx_now,y_now,dy_now)

    for element in f.__dict__.keys(): # pour eviter erreurs de code
        if hasattr(f.__dict__[element],'primal'):
            f.__dict__[element]=f.__dict__[element].primal

    y0=f.output(x0,0.,*P)
    dy0=jvp(f.output,(x0,0.,*P),(dx0,0.,*dP))[1]
    vect,(xf,dxf,yf,dyf)=scan(scan_fun,(x0,dx0,y0,dy0,
                        vect_t[0]),vect_t[1:])

    xf=np.transpose(np.concatenate((x0[None], xf)))
    yf=np.transpose(np.concatenate((y0[None], yf)))
    dxf=np.transpose(np.concatenate((dx0[None], dxf)))
    dyf = np.transpose(np.concatenate((dy0[None], dyf)))

    return xf,dxf,yf,dyf


def get_indice(names,valeur,output):
    if len(output)==1:
        return valeur[names.index(output[0])]
    else:
        return (valeur[names.index(i)] for i in output)
