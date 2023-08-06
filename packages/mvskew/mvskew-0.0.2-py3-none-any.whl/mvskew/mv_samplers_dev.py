#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:38:53 2020

@author: sven
"""

mst.dp2cp <- function(dp, cp.type="proper", fixed.nu=NULL, symmetr=FALSE, 
   aux=FALSE, upto=NULL)
{# dp2cp for multivariate ST, returns NULL if CP not found (implicitly silent)
  nu <- if(is.null(fixed.nu)) dp$nu else fixed.nu
  if(is.null(upto)) upto <- 4L
  if((round(upto) != upto)||(upto < 1)) stop("'upto' must be positive integer")
  if(nu <= upto && (cp.type =="proper")) return(NULL)
  if(cp.type == "proper")  {
    if(nu <= upto) 
      # stop(gettextf("d.f. '%s' too small, CP is undefined", nu), domain = NA)
      return(NULL)
      a <- rep(0, upto) 
      tilde <- NULL
    } else {
      a <- (1:upto) 
      tilde <- rep("~", upto)
    }
  Omega <- dp$Omega 
  d <- ncol(Omega)
  comp.names <- colnames(dp$Omega)
  alpha <- if(symmetr) rep(0, d) else dp$alpha 
  omega <- sqrt(diag(Omega))
  lot <- delta.etc(alpha, Omega)
  delta <- lot$delta
  delta.star <- lot$delta.star
  alpha.star <- lot$alpha.star
  comp.names <- colnames(dp$Omega)
  names(delta) <- comp.names  
  mu0 <- b(nu+a[1]) * delta * omega
  names(mu0) <- comp.names
  mu.2 <- b(nu+a[2]) * delta * omega
  if(is.vector(dp[[1]])) cp <- list(mean=dp[[1]] + mu0)  else {
    beta <- dp[[1]]  
    beta[1,] <- beta[1,] + mu0
    cp <- list(beta=beta)  }
  if(upto > 1) {
    Sigma <- Omega * (nu+a[2])/(nu+a[2]-2) - outer(mu.2, mu.2)
    dimnames(Sigma) <- list(comp.names, comp.names)
    cp$var.cov <- Sigma
    }
  cp$gamma1 <- if(upto > 2 & !symmetr) st.gamma1(delta, nu+a[3]) else NULL
  cp$gamma2M <- if(upto > 3 & is.null(fixed.nu))  
      mst.mardia(delta.star^2, nu+a[4], d)[2] else NULL
  names(cp) <- paste(names(cp), tilde[1:length(cp)], sep="")  
  # cp <- cp[1:length(dp1)]
  if(aux){
    mardia <- mst.mardia(delta.star^2, nu, d)
    cp$aux <- list(fixed.nu=fixed.nu, 
                omega=omega, Omega.cor=lot$Omega.cor, delta=delta,
                delta.star=delta.star, alpha.star=alpha.star, mardia=mardia)
    }
  return(cp)  
}
  
  
mst.dp2cp <- function(dp, cp.type="proper", fixed.nu=NULL, symmetr=FALSE, 
   aux=FALSE, upto=NULL)
{# dp2cp for multivariate ST, returns NULL if CP not found (implicitly silent)
  nu <- if(is.null(fixed.nu)) dp$nu else fixed.nu
  if(is.null(upto)) upto <- 4L
  if((round(upto) != upto)||(upto < 1)) stop("'upto' must be positive integer")
  if(nu <= upto && (cp.type =="proper")) return(NULL)
  if(cp.type == "proper")  {
    if(nu <= upto) 
      # stop(gettextf("d.f. '%s' too small, CP is undefined", nu), domain = NA)
      return(NULL)
      a <- rep(0, upto) 
      tilde <- NULL
    } else {
      a <- (1:upto) 
      tilde <- rep("~", upto)
    }
  Omega <- dp$Omega 
  d <- ncol(Omega)
  comp.names <- colnames(dp$Omega)
  alpha <- if(symmetr) rep(0, d) else dp$alpha 
  omega <- sqrt(diag(Omega))
  lot <- delta.etc(alpha, Omega)
  delta <- lot$delta
  delta.star <- lot$delta.star
  alpha.star <- lot$alpha.star
  comp.names <- colnames(dp$Omega)
  names(delta) <- comp.names  
  mu0 <- b(nu+a[1]) * delta * omega
  names(mu0) <- comp.names
  mu.2 <- b(nu+a[2]) * delta * omega
  if(is.vector(dp[[1]])) cp <- list(mean=dp[[1]] + mu0)  else {
    beta <- dp[[1]]  
    beta[1,] <- beta[1,] + mu0
    cp <- list(beta=beta)  }
  if(upto > 1) {
    Sigma <- Omega * (nu+a[2])/(nu+a[2]-2) - outer(mu.2, mu.2)
    dimnames(Sigma) <- list(comp.names, comp.names)
    cp$var.cov <- Sigma
    }
  cp$gamma1 <- if(upto > 2 & !symmetr) st.gamma1(delta, nu+a[3]) else NULL
  cp$gamma2M <- if(upto > 3 & is.null(fixed.nu))  
      mst.mardia(delta.star^2, nu+a[4], d)[2] else NULL
  names(cp) <- paste(names(cp), tilde[1:length(cp)], sep="")  
  # cp <- cp[1:length(dp1)]
  if(aux){
    mardia <- mst.mardia(delta.star^2, nu, d)
    cp$aux <- list(fixed.nu=fixed.nu, 
                omega=omega, Omega.cor=lot$Omega.cor, delta=delta,
                delta.star=delta.star, alpha.star=alpha.star, mardia=mardia)
    }
  return(cp)  
}
  
st.gamma1 <- function(delta, nu)
{# this function is vectorized for delta, works for a single value of nu
  if(length(nu) > 1) stop("'nu' must be a single value")
  if(nu <= 0) stop("'nu' must be positive")
  out <- rep(NaN, length(delta)) 
  ok <- (abs(delta) <= 1) 
  if((nu >= 3) & (sum(ok) > 0)) {
    alpha <- delta[ok]/sqrt(1 - delta[ok]^2)
    cum <- st.cumulants(0, 1, alpha, nu, n=3)
    out[ok] <- if(sum(ok) == 1) cum[3]/cum[2]^1.5 else cum[,3]/cum[,2]^1.5  
    }
  return(out) 
}
  
  
mst.mardia <- function(delta.sq, nu, d) 
{# Mardia measures gamma1 and gamma2 for MST; book: (6.31), (6.32), p.178
  if(d < 1) stop("d < 1") 
  if(d != round(d)) stop("'d' must be a positive integer")
  if(delta.sq < 0 | delta.sq > 1)  stop("delta.sq not in (0,1)")
  if(nu <= 3) stop("'nu>3' is required")
  cum <- st.cumulants(0, 1, sqrt(delta.sq/(1-delta.sq)), nu)
  mu <- cum[1]
  sigma <- sqrt(cum[2])
  gamma1 <- cum[3]/sigma^3
  gamma2 <- cum[4]/sigma^4
  gamma1M <- if(nu > 3) (gamma1^2 + 3*(d-1)*mu^2/((nu-3)*sigma^2)) else Inf
  r <- function(nu, k1, k2) 1/(1 - k2/nu) - k1/(nu - k2) # (nu-k1)/(nu-k2)
  gamma2M <- if(nu > 4) (gamma2 + 3 +(d^2-1)*r(nu,2,4) +2*(d-1)*(r(nu,0,4)
                -mu^2*r(nu,1,3))/sigma^2 - d*(d+2)) else Inf
  return(c(gamma1M=gamma1M, gamma2M=gamma2M))            
}    
    
cp2dp <- function(cp, family){
  family <- toupper(family)
  if(!(family %in% c("SN", "ESN", "ST","SC")))
      stop(gettextf("family '%s' is not supported", family), domain = NA)
  dp <- if(is.list(cp))  cp2dpMv(cp, family)  else cp2dpUv(cp, family)
  if(anyNA(dp)) dp <- NULL
  return(dp)
}
 
cp2dpUv <- function(cp, family, silent=FALSE, tol=1e-8) 
{ # internal function; works also with regression parameters included
   family <- toupper(family)
   if(family=="ESN") stop("cp2dp for ESN not yet implemented")
   if(family == "SN") {     
     p <- length(cp)-2-as.numeric(family=="ESN")
     beta1 <- if (p>1) cp[2:p] else NULL
     b <- sqrt(2/pi) 
     sigma  <- cp[p+1]
     excess <- max(0, -sigma)
     gamma1 <- cp[p+2]
     tau <- if(family=="ESN") as.numeric(cp[p+3]) else 0
     max.gamma1 <- 0.5*(4-pi)*(2/(pi-2))^1.5
     if (abs(gamma1) >= max.gamma1) {
       if (silent) excess <- excess + (abs(gamma1) - max.gamma1) else 
         {message("gamma1 outside admissible range"); return(invisible())}}
     if(excess > 0) {
       out <- NA
       attr(out, "excess") <- excess
       return(out)
       }
     r  <- sign(gamma1)*(2*abs(gamma1)/(4-pi))^(1/3)
     delta <- r/(b*sqrt(1+r^2))
     alpha <- delta/sqrt(1-delta^2)
     mu.z <- b*delta
     sd.z <- sqrt(1-mu.z^2)
     beta <- cp[1:p]
     omega <- cp[p+1]/sd.z
     beta[1] <- cp[1] - omega*mu.z
     dp <- as.numeric(c(beta, omega, alpha))
     names(dp) <- param.names("DP", family, p, x.names=names(beta1))
     return(dp)
     }
  if(family == "ST") return(st.cp2dp(cp, silent=silent, tol=tol))
  if(family == "SC") stop("this makes no sense for SC family")
  warning(gettextf("family = '%s' is not supported", family), domain = NA)
  invisible(NULL)
}

cp2dpMv <- function(cp, family, silent=FALSE, tol=1e-8) 
{ # internal function
  if(family == "SN")  dp <- msn.cp2dp(cp, silent)
  else if(family == "ESN") stop("cp2dp for ESN not yet implemented")
  else if(family == "ST") dp <- mst.cp2dp(cp, silent, tol=tol)
  else if(family == "SC") stop("this makes no sense for SC family")
  else warning(gettextf("family = '%s' is not supported", family), domain = NA)
  return(dp)
}

rmst <- function(n=1, xi=rep(0,length(alpha)), Omega, alpha, nu=Inf, dp=NULL)
{ 
  if(!(missing(alpha) & missing(Omega)) && !is.null(dp)) 
       stop("You cannot set both component parameters and dp")
  if(!is.null(dp)){
      if(!is.null(dp$xi)) xi <- dp$xi
        else
      if(!is.null(dp$beta)) xi <- as.vector(dp$beta)
      Omega <- dp$Omega
      alpha <- dp$alpha
      nu <- dp$nu
     }  
  if(any(abs(alpha) == Inf)) stop("Inf's in alpha are not allowed")
  d <- length(alpha)
  x <- if(nu==Inf) 1 else rchisq(n,nu)/nu
  z <- rmsn(n, rep(0,d), Omega, alpha)
  y <- t(xi+ t(z/sqrt(x)))
  attr(y, "family") <- "ST"
  attr(y, "parameters") <- list(xi=xi, Omega=Omega, alpha=alpha, nu=nu)
  return(y)
}
  
rmsn <- function(n=1, xi=rep(0,length(alpha)), Omega, alpha, tau=0, dp=NULL)
{# generates SN_d(..) variates using the additive (=transformation) method
  # if(!(missing(alpha) & missing(Omega) & !is.null(dp)))
  #     stop("You cannot set both component parameters and dp")
  if(!is.null(dp)) {  
     dp0 <- dp  
     dp0$nu <- NULL
     if(is.null(dp0$tau)) dp0$tau <- 0 
     if(names(dp)[1] == "beta") {
        dp0[[1]] <- as.vector(dp[[1]])
        names(dp0)[1] <- "xi"
        } 
     }
  else dp0 <- list(xi=xi, Omega=Omega, alpha=alpha, tau=tau)
  if(any(abs(dp0$alpha) == Inf)) stop("Inf's in alpha are not allowed")
  lot <- dp2cpMv(dp=dp0, family="SN", aux=TRUE)
  d <- length(dp0$alpha)
  y <- matrix(rnorm(n*d), n, d) %*% chol(lot$aux$Psi) # each row is N_d(0,Psi)
  if(dp0$tau == 0)    
    truncN <- abs(rnorm(n))  
  else 
    truncN <- qnorm(runif(n, min=pnorm(-dp0$tau), max=1))
  truncN <- matrix(rep(truncN, d), ncol=d)
  delta  <- lot$aux$delta
  z <- delta * t(truncN) + sqrt(1-delta^2) * t(y)
  y <- t(dp0$xi + lot$aux$omega * z)
  attr(y, "family") <- "SN"
  attr(y, "parameters") <- dp0
  return(y)
}
     
     dp2cpMv <- 
function(dp, family, cp.type="proper", fixed.nu=NULL, aux=FALSE, upto=NULL) 
{# internal. NB: name of cp[1] must change according to dp[1]
  cp.type <- match.arg(cp.type, c("proper", "pseudo", "auto"))
  family <- toupper(family)
  if(!(family %in% c("SN", "ESN", "ST","SC")))
    stop(gettextf("family '%s' is not supported", family), domain = NA)
  if(family %in% c("SN","ESN")){  
    if(cp.type == "pseudo") 
      warning("'cp.type=pseudo' makes no sense for SN and ESN families")
    cp <- msn.dp2cp(dp, aux=aux)
    if(!is.null(upto)) cp <- cp[1:upto]
    }
  if(family %in% c("SC","ST")){
    if(cp.type=="auto") cp.type <- 
      if(family == "SC" || dp[[4]] <= 4) "pseudo" else "proper"
    if(family == "SC") fixed.nu <- 1
    cp <- mst.dp2cp(dp, cp.type=cp.type, fixed.nu=fixed.nu, aux=aux, upto=upto)
    if(is.null(cp)) {warning("no CP could be found"); return(invisible())}
    }
  return(cp)
}
  
  
delta.etc <- function(alpha, Omega=NULL) 
{ 
  inf <- which(abs(alpha) == Inf)
  if(is.null(Omega)){ # case d=1
    delta <- alpha/sqrt(1+alpha^2)
    delta[inf] <- sign(alpha[inf])
    return(delta)
    }
  else { # d>1
    if(any(dim(Omega) != rep(length(alpha),2))) stop("dimension mismatch")
    Ocor <- cov2cor(Omega)
    if(length(inf) == 0) { # d>1, standard case
      Ocor.alpha <- as.vector(Ocor %*% alpha)
      alpha.sq <- sum(alpha * Ocor.alpha)
      delta <- Ocor.alpha/sqrt(1+alpha.sq)
      alpha. <- sqrt(alpha.sq)
      delta. <- sqrt(alpha.sq/(1+alpha.sq))
      }
     else { # d>1, case with some abs(alpha)=Inf
       if(length(inf) > 1) 
         warning("Several abs(alpha)==Inf, I handle them as 'equal-rate Inf'") 
       k <- rep(0,length(alpha))
       k[inf] <- sign(alpha[inf])
       Ocor.k <- as.vector(Ocor %*% k) 
       delta <- Ocor.k/sqrt(sum(k * Ocor.k))
       delta. <- 1
       alpha. <- Inf
       }
  return(
    list(delta=delta, alpha.star=alpha., delta.star=delta., Omega.cor=Ocor))
  }
}
  
msn.dp2cp <- function(dp, aux=FALSE)
{# dp2cp for multivariate SN and ESN 
  alpha <- dp$alpha
  d <- length(alpha)
  Omega <- matrix(dp$Omega, d, d)  
  omega <- sqrt(diag(Omega))
  lot <- delta.etc(alpha, Omega)
  delta <- lot$delta
  delta.star <- lot$delta.star
  alpha.star <- lot$alpha.star
  names(delta) <- names(dp$alpha)
  tau <- if(is.null(dp$tau)) 0 else dp$tau
  mu.z  <- zeta(1, tau) * delta
  sd.z  <- sqrt(1 + zeta(2, tau) * delta^2)
  Sigma <- Omega + zeta(2,tau) * outer(omega*delta, omega*delta)
  gamma1 <- zeta(3, tau) * (delta/sd.z)^3
  if(is.vector(dp[[1]])) { 
    cp <- list(mean=dp[[1]] + mu.z*omega, var.cov=Sigma, gamma1=gamma1)
    }
  else {
    beta <- dp[[1]]  
    beta[1,] <- beta[1,] + mu.z*omega
    cp <- list(beta=beta, var.cov=Sigma, gamma1=gamma1)
  }
  if(!is.null(dp$tau)) cp$tau <- tau
  if(aux){
    lambda <- delta/sqrt(1-delta^2)
    D <- diag(sqrt(1+lambda^2), d, d)
    Ocor <- lot$Omega.cor
    Psi <- D %*% (Ocor-outer(delta,delta)) %*% D
    Psi <- (Psi + t(Psi))/2
    O.inv <- pd.solve(Omega)
    O.pcor <- -cov2cor(O.inv) 
    O.pcor[cbind(1:d, 1:d)] <- 1
    R <- force.symmetry(Ocor + zeta(2,tau)*outer(delta,delta))
    ratio2 <- delta.star^2/(1+zeta(2,tau)*delta.star^2)
    mardia <- c(gamma1M=zeta(3,tau)^2*ratio2^3, gamma2M=zeta(4,tau)*ratio2^2)
    # SN book: see (5.74), (5.75) on p.153
    cp$aux <- list(omega=omega, cor=R, Omega.inv=O.inv, Omega.cor=Ocor, 
      Omega.pcor=O.pcor, lambda=lambda, Psi=Psi, delta=delta, lambda=lambda,
      delta.star=delta.star, alpha.star=alpha.star, mardia=mardia)
    }
  return(cp)  
}
  
zeta <- function(k, x)
{ # k integer in (0,5)
  if(k<0 | k>5 | k != round(k)) return(NULL)
  na <- is.na(x)
  x  <- replace(x,na,0)
  x2 <- x^2
  z <- switch(k+1,
            pnorm(x, log.p=TRUE) + log(2),           
            ifelse(x>(-50), exp(dnorm(x, log=TRUE) - pnorm(x, log.p=TRUE)),
                            -x/(1 -1/(x2+2) +1/((x2+2)*(x2+4)) 
                              -5/((x2+2)*(x2+4)*(x2+6))
                              +9/((x2+2)*(x2+4)*(x2+6)*(x2+8)) 
                              -129/((x2+2)*(x2+4)*(x2+6)*(x2+8)*(x2+10)) )), 
            (-zeta(1,x)*(x+zeta(1,x))),
            (-zeta(2,x)*(x+zeta(1,x)) - zeta(1,x)*(1+zeta(2,x))),
            (-zeta(3,x)*(x+2*zeta(1,x)) - 2*zeta(2,x)*(1+zeta(2,x))),
            (-zeta(4,x)*(x+2*zeta(1,x)) -zeta(3,x)*(3+4*zeta(2,x))
                 -2*zeta(2,x)*zeta(3,x)),
            NULL)
  neg.inf <- (x == -Inf)
  if(any(neg.inf))
    z <- switch(k+1,
                z,
                replace(z, neg.inf, Inf),
                replace(z, neg.inf, -1),
                replace(z, neg.inf, 0),
                replace(z, neg.inf, 0),
                replace(z, neg.inf, 0),
                NULL)
  if(k>1) z<- replace(z, x==Inf, 0)
  replace(z, na, NA)
}
  
force.symmetry <- function(x, tol=10*sqrt(.Machine$double.eps)) 
{
  if(!is.matrix(x)) stop("x must be a matrix")
  # err <- abs(x-t(x))
  err <- abs(x-t(x))/(1+abs(x))
  max.err <- max(err/(1+err))
  if(max.err > tol) warning("matrix seems not symmetric")
  if(max.err > 100*tol) stop("this matrix really seems not symmetric")
  return((x + t(x))/2)
}
  
import numpy as np 
import warnings
import scipy.stats as spp

rmsn <- function(n=1, xi=rep(0,length(alpha)), Omega, alpha, tau=0, dp=NULL)
{# generates SN_d(..) variates using the additive (=transformation) method
  # if(!(missing(alpha) & missing(Omega) & !is.null(dp)))
  #     stop("You cannot set both component parameters and dp")
  if(!is.null(dp)) {  
     dp0 <- dp  
     dp0$nu <- NULL
     if(is.null(dp0$tau)) dp0$tau <- 0 
     if(names(dp)[1] == "beta") {
        dp0[[1]] <- as.vector(dp[[1]])
        names(dp0)[1] <- "xi"
        } 
     }
  else dp0 <- list(xi=xi, Omega=Omega, alpha=alpha, tau=tau)
  if(any(abs(dp0$alpha) == Inf)) stop("Inf's in alpha are not allowed")
  lot <- dp2cpMv(dp=dp0, family="SN", aux=TRUE)
  d <- length(dp0$alpha)
  y <- matrix(rnorm(n*d), n, d) %*% chol(lot$aux$Psi) # each row is N_d(0,Psi)
  if(dp0$tau == 0)    
    truncN <- abs(rnorm(n))  
  else 
    truncN <- qnorm(runif(n, min=pnorm(-dp0$tau), max=1))
  truncN <- matrix(rep(truncN, d), ncol=d)
  delta  <- lot$aux$delta
  z <- delta * t(truncN) + sqrt(1-delta^2) * t(y)
  y <- t(dp0$xi + lot$aux$omega * z)
  attr(y, "family") <- "SN"
  attr(y, "parameters") <- dp0
  return(y)
}
     
     b <- function(nu)  # function b(.) in SN book, eq.(4.15)
{# vectorized for 'nu', intended for values nu>1, otherwise it returns NaN
   out <- rep(NaN, length(nu))
   big <- (nu > 1e4)
   ok  <- ((nu > 1) & (!big) & (!is.na(nu)))  
   # for large nu use asymptotic expression (from SN book, exercise 4.6)
   out[big] <- sqrt(2/pi) * (1 + 0.75/nu[big] + 0.78125/nu[big]^2)
   out[ok] <-  sqrt(nu[ok]/pi) * exp(lgamma((nu[ok]-1)/2) - lgamma(nu[ok]/2))
   return(out)
}
#
st.gamma1 <- function(delta, nu)
{# this function is vectorized for delta, works for a single value of nu
  if(length(nu) > 1) stop("'nu' must be a single value")
  if(nu <= 0) stop("'nu' must be positive")
  out <- rep(NaN, length(delta)) 
  ok <- (abs(delta) <= 1) 
  if((nu >= 3) & (sum(ok) > 0)) {
    alpha <- delta[ok]/sqrt(1 - delta[ok]^2)
    cum <- st.cumulants(0, 1, alpha, nu, n=3)
    out[ok] <- if(sum(ok) == 1) cum[3]/cum[2]^1.5 else cum[,3]/cum[,2]^1.5  
    }
  return(out) 
}
#     
st.gamma2 <- function(delta, nu) 
{# this function is vectorized for delta, works for a single value of nu
  if(length(nu) > 1) stop("'nu' must be a single value")
  if(nu <= 0) stop("'nu' must be positive")
  out <- rep(NaN, length(delta)) 
  ok <- (abs(delta) <= 1)
  if((nu >= 4) & (sum(ok) > 0)) {
    alpha <- delta[ok]/sqrt(1 - delta[ok]^2)
    cum <- st.cumulants(0, 1, alpha, nu, n=4)
    out[ok] <- if(sum(ok) == 1) cum[4]/cum[2]^2 else cum[,4]/cum[,2]^2
    }
  return(out)  
}
  
st.cumulants <- function(xi=0, omega=1, alpha=0, nu=Inf, dp=NULL, n=4)
{
  if(!is.null(dp)) {
      if(!missing(alpha)) 
        stop("You cannot set both 'dp' and the component parameters")
      xi <- dp[1]
      omega <- dp[2]
      alpha <- dp[3]
      nu <- dp[4]
      }
  if(length(nu) > 1) stop("'nu' must be a scalar value")    
  if(nu == Inf) return(sn.cumulants(xi, omega, alpha, n=n))
  n <- min(as.integer(n), 4)      
  par <- cbind(xi, omega, alpha)
  alpha <- par[,3]
  delta <- ifelse(abs(alpha)<Inf, alpha/sqrt(1+alpha^2), sign(alpha))
  cum <- matrix(NaN, nrow=nrow(par), ncol=n)
  cum[,1] <- mu <- b(nu)*delta
  # r <- function(nu, k1, k2) 1/(1-k2/nu) - k1/(nu-k2)     # = (nu-k1)/(nu-k2)
  s <- function(nu, k) 1/(1 - k/nu)                        # = nu/(nu-k)
  if(n>1 & nu>2) cum[,2] <- s(nu,2) - mu^2
  if(n>2 & nu>3) cum[,3] <- np.multiply(mu,(3-delta^2)*s(nu,3) - 3*s(nu,2) + 2*mu^2)
  if(n>2 & nu==3) cum[,3] <- sign(alpha) * Inf  
  if(n>3 & nu>4) cum[,4] <- (3*s(nu,2)*s(nu,4) - 4*mu^2*(3-delta^2)*s(nu,3)
                             + 6*mu^2*s(nu,2)-3*mu^4) - 3*cum[,2]^2
  if(n>3 & nu==4) cum[,4] <- Inf
  cum <- cum*outer(par[,2], 1:n, "^")
  cum[,1] <- cum[,1]+par[,1]
  cum[,,drop=TRUE]
}
     
import timeit 
df = 1
size = 200
t = timeit.time.time()
multivariate_T_sampler(xi,Omega,df,size=size)
tdiv = t = timeit.time.time()-t
t = timeit.time.time()
multivariate_T_sampler(xi,Omega,df,size=size,calcopt='SVD')
tsvd = t = timeit.time.time()-t

op2dp <- function(op, family) 
{
  nt <- switch(tolower(family), "sn" = 3, "esn" = 4, "st" = 4, "sc" = 3, NULL)
  if(is.null(nt)) stop("unknown family")
  dp <- op
  if(is.list(op)) { # multivariate case 
    if(length(op) != nt) stop("wrong length of 'op'")
    Psi <- op[[2]] 
    psi <- sqrt(diag(Psi))
    lambda <- op[[3]]
    delta <- lambda/sqrt(1 + lambda^2)
    D.delta <- sqrt(1 - delta^2)
    Psi.bar <- cov2cor(Psi)
    omega <- psi/D.delta
    tmp <- as.vector(pd.solve(Psi.bar) %*% lambda)
    dp[[2]] <- Psi + outer(psi*lambda, psi*lambda)  # four lines before (5.30)
    dp[[3]] <- (tmp/D.delta)/sqrt(1 + sum(lambda*tmp))  # (5.22)
    names(dp)[2:3] <- c("Omega", "alpha")
    } 
  else { # univariate case
    p <- length(op) - nt + 1
    if(p < 1) stop("wrong length of 'dp'")
    delta <- delta.etc(dp[p+2])
    dp[p+1] <- op[p+1]/sqrt(1 - delta^2)
    names(dp)[(p+1):(p+2)] <- c("omega", "alpha")
    }  
  dp
}
  
cp2dp <- function(cp, family){
  family <- toupper(family)
  if(!(family %in% c("SN", "ESN", "ST","SC")))
      stop(gettextf("family '%s' is not supported", family), domain = NA)
  dp <- if(is.list(cp))  cp2dpMv(cp, family)  else cp2dpUv(cp, family)
  if(anyNA(dp)) dp <- NULL
  return(dp)
}

cp2dpMv <- function(cp, family, silent=FALSE, tol=1e-8) 
{ # internal function
  if(family == "SN")  dp <- msn.cp2dp(cp, silent)
  else if(family == "ESN") stop("cp2dp for ESN not yet implemented")
  else if(family == "ST") dp <- mst.cp2dp(cp, silent, tol=tol)
  else if(family == "SC") stop("this makes no sense for SC family")
  else warning(gettextf("family = '%s' is not supported", family), domain = NA)
  return(dp)
}


msn.cp2dp <- function(cp, silent=FALSE) {
  beta <- cp[[1]]
  Sigma <- cp[[2]]
  gamma1 <- cp[[3]]
  d <- length(gamma1)
  b <- sqrt(2/pi)  
  max.gamma1 <- 0.5*(4-pi)*(2/(pi-2))^1.5
  if(any(abs(gamma1) >= max.gamma1))  
    {if(silent) return(NULL) else stop("non-admissible CP")}
  R <- sign(gamma1)*(2*abs(gamma1)/(4-pi))^(1/3)
  delta <-  R/(b*sqrt(1+R^2))
  mu.z <- b*delta
  omega <- sqrt(diag(Sigma)/(1-mu.z^2))
  Omega <- Sigma + outer(mu.z*omega, mu.z*omega)
  Omega.bar <- cov2cor(Omega)
  Obar.inv <- pd.solve(Omega.bar, silent=silent)
  if(is.null(Obar.inv))  
    {if(silent) return(NULL) else stop("non-admissible CP")}
  Obar.inv.delta <- as.vector(Obar.inv %*% delta)
  delta.sq <- sum(delta * Obar.inv.delta)
  if(delta.sq >= 1) 
    {if(silent) return(NULL) else stop("non-admissible CP")}
  alpha <- Obar.inv.delta/sqrt(1-delta.sq)
  if(is.vector(beta)) {
    beta <- beta - omega*mu.z
    dp <- list(beta=beta, Omega=Omega, alpha=alpha)
    }
  else {
    beta[1,] <- beta[1,] - omega*mu.z
    dp <- list(beta=beta, Omega=Omega, alpha=alpha)  
    }
  attr(dp, "delta.star") <- sqrt(delta.sq)
  return(dp)
  }
  
mst.cp2dp <- function(cp, silent=FALSE, tol=1e-8, trace=FALSE) 
{
  mu <- drop(cp[[1]])
  Sigma <- cp[[2]]
  gamma1 <- cp[[3]]
  gamma2M <- cp[[4]]
  d <- length(gamma1)
  # fn1 <- function(delta, g1, nu) st.gamma1(delta, nu) - g1
  # fn2 <- function(log.nu, g2, delta.sq, d)
  #                mst.gamma2M(delta.sq, exp(log.nu), d) - g2
  if(any(abs(gamma1) >= 4)) 
    {if(silent) return(NULL) else stop("cp$gamma1 not admissible")}
  dp.marg <- matrix(NA, d, 4)
  for(j in 1:d) {  
     dp <- st.cp2dp(c(0,1,gamma1[j], gamma2M), silent=silent)
     if(is.null(dp)) 
       {if(silent) return(NULL) else stop("no CP could be found")}
     dp.marg[j,] <- dp
  }
  if(trace) {cat("starting dp:\n"); print(dp.marg)}
  fn <- function(par, Sigma, gamma1, gamma2M, trace=FALSE){
    if(trace)  cat("[mst.cp2dp[fn]] par:", format(par), "\n")
    nu <- exp(par[1])+4
    delta <- par[-1]/sqrt(1+par[-1]^2)
    d <- length(delta)
    mu.z <- delta*b(nu)
    omega <- sqrt(diag(Sigma)/(nu/(nu-2)-mu.z^2))
    Omega.bar <- (diag(1/omega, d, d) %*% Sigma %*% diag(1/omega, d, d)
                   + outer(mu.z, mu.z)) * (nu-2)/nu
    Obar.inv <- pd.solve(force.symmetry(Omega.bar))
    delta.sq <- sum(delta * as.vector(Obar.inv %*% delta))
    if(delta.sq >= 1) return(delta.sq*10^10)
    L1 <- sum((st.gamma1(delta, nu) - gamma1)^2)
    L2 <- (mst.mardia(delta.sq, nu, d)[2] - gamma2M)^2
    # if(trace){  ecat(c(nu,delta,L1,L2))} # ; readline("<cr>")}
    L1 + L2
    }
  nu <- min(dp.marg[,4])
  par <- c(log(nu-4), dp.marg[,3])
  if(trace) cat("[mst.cp2dp] par:", format(par), "\n")
  opt <- nlminb(par, fn, Sigma=Sigma, gamma1=gamma1, gamma2M=gamma2M,
                trace=trace)
  if(trace) cat("[mst.cp2dp]\nopt$convergence:", opt$convergence, 
                "\nopt$message", opt$message, "\n")
  if(opt$convergence != 0) 
    { if(silent) return(NULL) else stop ("no CP could be found") }
  par <- opt$par
  nu <- exp(par[1])+4
  delta <- par[-1]/sqrt(1+par[-1]^2)
  if(trace) {
    cat("[mst.cp2dp]min opt$fn:", format(opt$obj),"\n")
    print(c(nu,delta))
    }
  mu.z <- delta*b(nu)
  omega<- sqrt(diag(Sigma)/(nu/(nu-2)-mu.z^2))
  Omega.bar <- (diag(1/omega, d, d) %*% Sigma %*% diag(1/omega, d, d)
                   + outer(mu.z,mu.z)) * (nu-2)/nu
  Obar.inv <- pd.solve(Omega.bar)
  delta.sq <- sum(delta * as.vector(Obar.inv %*% delta))
  alpha <- as.vector(Obar.inv %*% delta)/sqrt(1-delta.sq)
  if(is.matrix(mu)) {
     xi <- mu
     xi[1,] <- mu[1,] - omega*mu.z }
  else xi <- mu - omega*mu.z
  Omega <- diag(omega) %*% Omega.bar %*% diag(omega)
  return(list(xi=xi, Omega=Omega, alpha=alpha, nu=nu))
}


def _check_format(x):
    
    if type(x) == np.matrix:
        x = np.array(x)
        
    if len(x.shape) > 1:
        x = x.reshape(-1)
        
    return(x)
    
import scipy.special as sps   

def op2dp(xi, Psi, lambhdha): 
    
    if type(xi) in [int,float,np.int_,np.float_]:
        
        delta = delta_etc(xi)
        Omega = np.divide(Psi,np.sqrt(1 - np.square(delta)))
        alpha = lambhdha
        
    else:
        
        psi = np.sqrt(np.diag(Psi))
        delta = np.divide(lambhdha,np.sqrt(1 + np.square(lambhdha)))
        D_delta = np.sqrt(1 - np.square(delta))
        Psi_bar = cov2cor(Psi)
        omega = np.divide(psi,D_delta)
        tmp = np.matmul(np.linalg.inv(Psi_bar),lambhdha)
        Omega = Psi + np.outer(np.multiply(psi,lambhdha), np.multiply(psi,lambhdha))  # four lines before (5.30)
        alpha = np.divide(np.divide(tmp,D_delta),np.sqrt(1 + np.sum(np.multiply(lambhdha,tmp))))  # (5.22)
        
    return(xi,Omega,alpha)
    
    
def msn_cp2dp(beta,Sigma,gamma1,verbose=False):
    
    beta = _check_format(beta)
    gamma1 = _check_format(gamma1)
    d = gamma1.shape[0]
    b = np.sqrt(2/np.pi)  
    max_gamma1 = 0.5*(4-np.pi)*np.power(2/(np.pi-2),1.5)
    if (np.abs(gamma1) >= max_gamma1).any():  
        if not(verbose): 
            return(None) 
        else: 
            raise(ValueError(f"Centred gamma 1 exceeds maximum {max_gamma1}"))
    R = np.multiply(np.sign(gamma1),np.power(2*np.abs(gamma1)/(4-np.pi),1/3))
    delta = np.divide(R,(b*np.sqrt(1+np.square(R))))
    mu_z = b*delta
    omega = np.sqrt(np.divide(np.diag(Sigma),(1-np.square(mu_z))))
    mu_zomega = np.multiply(mu_z,omega)
    Omega = Sigma + np.outer(mu_zomega, mu_zomega)
    Omega_bar = cov2cor(Omega)
    Obar_inv = np.linalg.inv(Omega_bar)
    if Obar_inv is None:  
        if not(verbose):
            return(None) 
        else: 
            raise(ValueError("non-admissible CP"))
    Obar_inv_delta = np.matmul(Obar_inv,delta)
    delta_sq = np.sum(np.multiply(delta,Obar_inv_delta))
    if delta_sq >= 1: 
        if not(verbose):
            return(None) 
        else: 
            raise(ValueError(f"CP entered leads to delta^2 {delta_sq} > 1"))
    alpha = np.divide(Obar_inv_delta,np.sqrt(1-delta_sq))
    beta -= np.multiply(omega,mu_z)
    
    return(beta,Omega,alpha,np.sqrt(delta_sq))
    

def mst_cp2dp(beta,Sigma,gamma1,gamma2M,verbose=False, tol=1e-8, trace=False): 

    beta = _check_format(beta)
    gamma1 = _check_format(gamma1)
    d = gamma1.shape[0]
  # fn1 <- function(delta, g1, nu) st.gamma1(delta, nu) - g1
  # fn2 <- function(log.nu, g2, delta.sq, d)
  #                mst.gamma2M(delta.sq, exp(log.nu), d) - g2
    if (np.abs(gamma1) >= 4).any(): 
        if verbose:  
            raise(ValueError("cp$gamma1 not admissible")
        else:
            return(None)
            
    dp_marg = np.full((d,4),np.nan)
    for j in range(1,d):  
        dp = st_cp2dp(c(0,1,gamma1[j], gamma2M), silent=silent)
     if(is.null(dp)) 
       {if(silent) return(NULL) else stop("no CP could be found")}
     dp.marg[j,] <- dp
  }
  if(trace) {cat("starting dp:\n"); print(dp.marg)}
  fn <- function(par, Sigma, gamma1, gamma2M, trace=FALSE){
    if(trace)  cat("[mst.cp2dp[fn]] par:", format(par), "\n")
    nu <- exp(par[1])+4
    delta <- par[-1]/sqrt(1+par[-1]^2)
    d <- length(delta)
    mu.z <- delta*b(nu)
    omega <- sqrt(diag(Sigma)/(nu/(nu-2)-mu.z^2))
    Omega.bar <- (diag(1/omega, d, d) %*% Sigma %*% diag(1/omega, d, d)
                   + outer(mu.z, mu.z)) * (nu-2)/nu
    Obar.inv <- pd.solve(force.symmetry(Omega.bar))
    delta.sq <- sum(delta * as.vector(Obar.inv %*% delta))
    if(delta.sq >= 1) return(delta.sq*10^10)
    L1 <- sum((st.gamma1(delta, nu) - gamma1)^2)
    L2 <- (mst.mardia(delta.sq, nu, d)[2] - gamma2M)^2
    # if(trace){  ecat(c(nu,delta,L1,L2))} # ; readline("<cr>")}
    L1 + L2
    }
  nu <- min(dp.marg[,4])
  par <- c(log(nu-4), dp.marg[,3])
  if(trace) cat("[mst.cp2dp] par:", format(par), "\n")
  opt <- nlminb(par, fn, Sigma=Sigma, gamma1=gamma1, gamma2M=gamma2M,
                trace=trace)
  if(trace) cat("[mst.cp2dp]\nopt$convergence:", opt$convergence, 
                "\nopt$message", opt$message, "\n")
  if(opt$convergence != 0) 
    { if(silent) return(NULL) else stop ("no CP could be found") }
  par <- opt$par
  nu <- exp(par[1])+4
  delta <- par[-1]/sqrt(1+par[-1]^2)
  if(trace) {
    cat("[mst.cp2dp]min opt$fn:", format(opt$obj),"\n")
    print(c(nu,delta))
    }
  mu.z <- delta*b(nu)
  omega<- sqrt(diag(Sigma)/(nu/(nu-2)-mu.z^2))
  Omega.bar <- (diag(1/omega, d, d) %*% Sigma %*% diag(1/omega, d, d)
                   + outer(mu.z,mu.z)) * (nu-2)/nu
  Obar.inv <- pd.solve(Omega.bar)
  delta.sq <- sum(delta * as.vector(Obar.inv %*% delta))
  alpha <- as.vector(Obar.inv %*% delta)/sqrt(1-delta.sq)
  if(is.matrix(mu)) {
     xi <- mu
     xi[1,] <- mu[1,] - omega*mu.z }
  else xi <- mu - omega*mu.z
  Omega <- diag(omega) %*% Omega.bar %*% diag(omega)
  return(list(xi=xi, Omega=Omega, alpha=alpha, nu=nu))
}


 

def multivariate_skew_T_sampler(xi, Omega, alpha, tau=0, df=1, size=1):
    
    # generates SN_d(..) variates using the additive (=transformation) method
    
    if ((type(df) not in [int,np.int_]) or (df <= 0)):
        raise(ValueError("Degrees of freedom must be a strictly positive integer"))
    if ((type(size) not in [int,np.int_]) or (size <= 0)):
        raise(ValueError("Size must be a strictly positive integer"))
    
    if type(tau) in [int,float,np.int_,np.float_]:
        tau = np.array([tau])
    
    xi = _check_format(xi)
    alpha = _check_format(alpha)
    tau = _check_format(tau)
    
    if (np.isinf(alpha).any()): 
        raise(ValueError("Inf's in alpha are not allowed"))
    d = alpha.shape[0]
    if (nu == np.infty):
        x = 1 
    else: 
        x = (spp.chi2.rvs(df,size=size)/df).reshape((size,1))
    z = multivariate_skewnormal_sampler(np.repeat(0,d), Omega, alpha, tau, size=size)
    y = np.repeat(xi.reshape((1,d)),size,axis=0) + np.divide(z,np.repeat(np.sqrt(x),d,axis=1))
    
    return(y)
     
def dp2cpMV(xi,Omega,alpha,tau=0, nu=np.infty, family='SN', cp_type="proper", aux=False, upto=4):
    
    family = family.upper()
    
    if (cp_type not in ("auto","proper","pseudo")):
        raise(ValueError("CP type '%s' is not supported", cp_type))
    
    if (family not in ("SN","ST","SC")):
        raise(ValueError("family '%s' is not supported", family))
        
    if (family is ("SN")):  
        if (cp_type == "pseudo"): 
            warnings.warn("'cp_type=pseudo' makes no sense for the skew normal family")
        cp = msn_dp2cp(xi,Omega,alpha,tau,aux=aux)
        
    if (family in ("SC","ST")):
        if(cp_type=="auto"): 
             if((family == "SC") or (nu <= 4)): 
                 cp_type = "pseudo" 
        else: 
                cp_type = "proper"
                
        if (family == "SC"): 
            nu = 1
        cp = mst_dp2cp(xi,Omega,alpha,tau,nu,upto,cp_type=cp_type,aux=aux)
    if (cp is None): 
        warnings.warn("no CP could be found")
    return(cp)
    
def mst_dp2cp(xi,Omega,alpha,tau=0,nu=1,upto=4,cp_type="proper", 
              symmetr=False, aux=False):
    
    """
    Transformation of direct distribution parameters to centred distribution 
    parameters for the skew T family. 
    Inputs: 
        xi, (n,), (n,1) or (1,n) matrix or array, location
        Omega, (n,n), matrix, Scale
        alpha, (n,), (n,1) or (1,n) matrix or array, skewness
        tau, (n,), (n,1) or (1,n) matrix or array, tau parameter(s)
        nu, int, degrees of freedom
        upto, int, number of moments to compute in correction (default = max =4)
        cp_type, str, type of centred parameters, "proper" or "approx"; 
            "proper" can only be computged if nu > upto
        symmetr, bool, to enforce symmetry. Defaults to False. 
        aux, bool, to report auxiliary estimates. 
    Output
        a tuple comtaining: transformed location, scale, skewness and input skewness
    Remark
        Works for univariate parameters, but they have to be entered as array 
        or matrix, e.g. 
        msn_dp2cp(np.array([1]),np.array([2]),np.array([1]))
    """
    
    xi = _check_format(xi)
    alpha = _check_format(alpha)
    tau = _check_format(tau)
    
    if((round(upto) != upto) or (upto < 1)): 
        raise(ValueError("'upto' must be positive integer"))
    if((nu <= upto) and (cp_type =="proper")): 
        warnings.warn("Proper type of correction cannot be computed if df < number of moments")
        return(None)
    if(cp_type == "proper"):
        if(nu <= upto): 
            warnings.warn("Centred parameters are not defined at " + str(nu) + " degrees of freedom")
            return(None)
        a = np.zeros(upto) 
    else:
        a = np.arange(1,upto+1) 
         
    d = Omega.shape[1]
    if symmetr:
        alpha = np.repeat(0,d) 
    omega = np.sqrt(np.diag(Omega))
    delta,alpha_star,delta_star,Ocor = delta_etc(alpha, Omega)
    mu0 = np.multiply(np.multiply(bleat(nu+a[0]),delta),omega)
    mu_2 = np.multiply(np.multiply(bleat(nu+a[1]),delta),omega)
    beta = xi + mu0
    if (upto > 1):
        Sigma = np.multiply(Omega,np.divide((nu+a[1]),(nu+a[1]-2))) - np.outer(mu_2, mu_2)
    else: 
        Sigma = Omega
    
    if ((upto > 2) and not(symmetr)):
        gamma1 =  st_gamma1(delta, nu+a[2]) 
    else: 
        gamma1 = None
    
    if (upto > 3):
        gamma2 =  mst_mardia(np.square(delta_star), nu+a[3], d)[1]
    else: 
        gamma2 = None
        
    if aux:
        if nu <= 3:
            warnings.warn("Mardia parameters can only be computed for df>=4")
            cp = (beta, Sigma, gamma1, gamma2, nu)
        else:
            mardia = mst_mardia(np.square(delta_star), nu, d)
            cp = (beta, Sigma, gamma1, gamma2, nu, omega, Ocor, delta,
                delta_star, alpha_star, mardia)
    else:
        cp = (beta, Sigma, gamma1, gamma2, nu)
        
    return(cp)
    
    
  
def mst_mardia(delta_sq, nu, d): 
    
    """
    Mardia measures gamma1 and gamma2 for MST; book: (6.31), (6.32), p.178
    """
    
    if (d < 1):
        raise(ValueError("d < 1")) 
    if (d != round(d)): 
        raise(ValueError("'d' must be a positive integer"))
    if ((delta_sq < 0) or (delta_sq > 1)):  
        raise(ValueError("delta.sq not in (0,1)"))
    if (nu <= 3): 
        raise(ValueError("'nu>3' is required"))
        
    cumul = st_cumulants(0, 1, np.sqrt(np.divide(delta_sq,(1-delta_sq))), nu).reshape((4,))
    mu = cumul[0]
    sigma = np.sqrt(cumul[1])
    gamma1 = np.divide(cumul[2],np.power(sigma,3))
    gamma2 = np.divide(cumul[3],np.power(sigma,4))
    if (nu > 3):
        gamma1M = np.square(gamma1) + 3*(d-1)*np.divide(np.square(mu),\
                             np.multiply((nu-3),np.square(sigma))) 
    else: 
        gamma1M = np.infty
    are = lambda nu, k1, k2: 1/(1 - k2/nu) - k1/(nu - k2) # (nu-k1)/(nu-k2)
    if (nu > 4):
        gamma2M = (gamma2 + 3 +(d**2-1)*are(nu,2,4) + 2*(d-1)*(are(nu,0,4)
                -np.square(mu)*are(nu,1,3))/np.square(sigma) - d*(d+2))
    else: 
        gamma2M = np.infty
        
    return(gamma1M,gamma2M)            
    
  
def st_gamma1(delta, nu):
    
    """
    Skew-t gamma 1 measure.
    Remark: this function is vectorized w.r.t. delta, but takes a single value of nu
    """
    
    if type(nu) == np.ndarray:
        if (nu.shape[0] > 1): 
            raise(ValueError("'nu' must be a single value"))
        nu = nu[0]
    if (nu <= 0): 
        raise(ValueError("'nu' must be positive"))
    out = np.repeat(np.nan, len(delta)) 
    ok = (np.abs(delta) <= 1) 
    if ((nu >= 3) and (np.sum(ok) > 0)): 
        alpha = np.divide(delta[ok],np.sqrt(1 - np.square(delta[ok])))
        cumul = st_cumulants(0, 1, alpha, nu, n=3) 
        if (np.sum(ok) == 1):
            out[ok] = cumul[2]/cumul[1]^1.5 
        else: 
            out[ok] = np.divide(cumul[:,2],np.power(cumul[:,1],1.5))  
    return(out)
    

      
def st_cumulants(xi=0, omega=1, alpha=0, nu=np.infty, n=4):
    
    """
    Calculates the skew T cumulants up to order 4 for given distribution parameters
    and degrees of freedom 
    """
    
    if type(nu) == np.ndarray:
        if (nu.shape[0] > 1): 
            raise(ValueError("'nu' must be a single value"))
        nu = nu[0]
    if type(alpha) == np.ndarray:
        d = alpha.shape[0]    
    elif type(alpha) in (int,float,np.int_,np.float_):
        d = 1
    else:
        raise(ValueError("Please provide xi as scalar or array"))
    if(np.isinf(nu)): 
        # return(sn.cumulants(xi, omega, alpha, n=n))
        raise(NotImplementedError("At nu=inf, sn cumulants ought to be returned. To be implemented"))
    n = min((n,4))      
    #  par = cbind(xi, omega, alpha)
    #  alpha <- par[,3]
    if (np.abs(alpha) < np.infty).all():
        delta = np.divide(alpha,np.sqrt(1+np.square(alpha)))
    else:
        delta = np.sign(alpha)
    cumul = np.full((d,n),np.nan)
    mu = np.multiply(bleat(nu),delta)
    cumul[:,0] = mu
    # r <- function(nu, k1, k2) 1/(1-k2/nu) - k1/(nu-k2)     # = (nu-k1)/(nu-k2)
    s = lambda nu, k: np.divide(1,(1 - np.divide(k,nu)))                        # = nu/(nu-k)
    if ((n>1) and (nu>2)): 
        cumul[:,1] = s(nu,2) - np.square(mu)
    if ((n>2) and (nu>3)): 
        cumul[:,2] = np.multiply(mu,(np.multiply(3-np.square(delta),s(nu,3)) - 3*s(nu,2) + 2*np.square(mu)))
    if ((n>2) and (nu==3)): 
        cumul[:,2] = np.sign(alpha) * np.infty  
    if ((n>3) and (nu>4)): 
        cumul[:,3] = 3*np.multiply(s(nu,2),s(nu,4)) \
                    - 4*np.multiply(np.square(mu),np.multiply(3-np.square(delta),s(nu,3))) \
                    + 6*np.multiply(np.square(mu),s(nu,2))-3*np.power(mu,4) \
                    - 3*np.square(cumul[:,1])
    if ((n>3) and (nu==4)): 
        cumul[:,3] = np.infty
    cumul = np.multiply(cumul,np.power.outer(omega,np.arange(1,n+1)))
    cumul[:,0] = cumul[:,0] + xi
    
    return(cumul)
  
def bleat(nu):  
    """
    function b(.) in SN book, eq.(4.15)
    longer name picked to avoid confusion
    vectorized for 'nu', intended for values nu>1, otherwise it returns NaN
    """  

    if type(nu) in (int,float,np.int_,np.float_):
        nu = np.array([nu])
    out = np.repeat(np.nan, len(nu))
    big = (nu > 1e4)
    ok = np.where(np.logical_and(np.logical_and(nu > 1, nu <= 1e4),np.equal(np.isnan(nu),False)))
    # for large nu use asymptotic expression (from SN book, exercise 4.6)
    out[big] = np.sqrt(2/np.pi)*(1+np.divide(0.75,nu[big])+np.divide(0.78125,np.square(nu[big])))
    out[ok] = np.multiply(np.sqrt(nu[ok]/np.pi),
       np.exp(sps.gammaln((nu[ok]-1)/2) - sps.gammaln(nu[ok]/2))
       )
    return(out)
     

def multivariate_skewnormal_sampler(xi, Omega, alpha, tau=np.array([0]), size=1):
    
    """
    Sample from a multivariate skew normal distribution based on the aditive 
    approach 
    Inputs: xi, (n,), (n,1) or (1,n) matrix or array, location
            Omega, (n,n), matrix, Scale
            alpha, (n,), (n,1) or (1,n) matrix or array, skewness
            tau, int, float, (1,), (1,1), (n,), (n,1) or (1,n), matrix or array, tau parameter(s)
            size, int, number of cases to sample
    Output: tha sample as a (size,n) matrix
    """
    
    if ((type(size) not in [int,np.int_]) or (size <= 0)):
        raise(ValueError("Size must be a strictly positive integer"))
    if type(tau) in [int,float,np.int_,np.float_]:
        tau = np.array([tau])
    
    xi = _check_format(xi)
    alpha = _check_format(alpha)
    tau = _check_format(tau)
    
    (beta, Sigma, gamma1, tau, omega, R, O_inv, Ocor, O_pcor, \
     lambhdha, Psi, delta, delta_star, alpha_star, gamma1M, gamma2M) = \
     msn_dp2cp(xi,Omega,alpha,tau,aux=True)
    d = alpha.shape[0]
    print(d)
    y = np.matmul(np.random.normal(size=(size,d)),np.linalg.cholesky(Psi)) # each row is N_d(0,Psi)
    
    if (tau==np.array([0])).all():  
        if (tau==np.array([0])).all():    
#        z = spp.norm.rvs(0,1,(size,d))
#        u = spp.norm.rvs(0,1,(size,d))
#        where_sign_flip = (u > alpha*z)
#        z[where_sign_flip] *= -1  
        z = np.array(np.matmul(np.random.normal(size=(size,d)),np.linalg.cholesky(Psi)))
        where_sign_flip = (np.abs(z) > np.array(gamma1).reshape(-1)*np.abs(np.array(y)))
        z[np.where(where_sign_flip)[0],:] *= -1
#        z = np.multiply(np.multiply(delta, z) + np.sqrt(1-np.square(delta)),y)
#        truncN = np.multiply(np.abs(spp.norm.rvs(0,1,(size,1))),np.sign(gamma1))
#        start = 0
#        truncN = spp.norm.ppf(spp.uniform.rvs(start,1-start,size=size))
#        truncN = np.tile(truncN.reshape((size,1)),(1,d))
#        z = np.multiply(np.multiply(delta, truncN) + np.sqrt(1-np.square(delta)),y)
        
    else: 
        start = spp.norm.cdf(-tau[0])
        truncN = spp.norm.ppf(spp.uniform.rvs(start,1-start,size=size))
        truncN = np.tile(truncN.reshape((size,1)),(1,d))
        z = np.multiply(np.multiply(delta, truncN) + np.sqrt(1-np.square(delta)),y)
    
    y = beta + np.multiply(omega,z)
    else: 
        start = spp.norm.cdf(-tau[0])
        truncN = spp.norm.ppf(spp.uniform.rvs(start,1-start,size=size))
        truncN = np.tile(truncN.reshape((size,1)),(1,d))
        z = np.multiply(np.multiply(delta, truncN) + np.sqrt(1-np.square(delta)),y)
    
    y = beta + np.multiply(omega,z)
    
    return(y)
  
  
def msn_dp2cp(xi,Omega,alpha,tau=0, aux=False): 
    
    """
    Transformation of direct distribution parameters to centred distribution 
    parameters for the skewnormal family. 
    Inputs: 
        xi, (n,), (n,1) or (1,n) matrix or array, location
        Omega, (n,n), matrix, Scale
        alpha, (n,), (n,1) or (1,n) matrix or array, skewness
        tau, (n,), (n,1) or (1,n) matrix or array, tau parameter(s)
        aux, bool, to report auxiliary estimates. 
    Output
        a tuple comtaining: transformed location, scale, skewness and input skewness
    Remark
        Works for univariate parameters, but they have to be entered as array 
        or matrix, e.g. 
        msn_dp2cp(np.array([1]),np.array([2]),np.array([1]))
    """
    
    xi = _check_format(xi)
    alpha = _check_format(alpha)
    tau = _check_format(tau)
        
    d = alpha.shape[0]
    Omega = np.matrix(Omega)  #maybe not necessary 
    omega = np.sqrt(np.diag(Omega))
    delta,alpha_star,delta_star,Ocor = delta_etc(alpha, Omega)
    mu_z = np.multiply(zeta(1, tau),delta)
    sd_z = np.sqrt(1 + np.multiply(zeta(2, tau),np.square(delta)))
    Sigma = Omega + np.multiply(zeta(2,tau),np.outer(np.multiply(omega,delta), np.multiply(omega,delta)))
    Sigma[np.tril_indices(d,k=-1)] = Sigma[np.triu_indices(d,k=1)] #only lower trianguilar in Azzalini
    gamma1 = np.multiply(zeta(3, tau),np.power(np.divide(delta,sd_z),3))
    if (type(alpha) == np.ndarray): #multivariate
        beta = xi + np.multiply(mu_z,omega)
        cp = (beta, Sigma, gamma1, tau)
    else: #univariate
        beta = xi + np.multiply(mu_z,omega)
        cp = (beta, Sigma, gamma1, tau)
    if(aux):
        if len(delta.shape)>1:
            if delta.shape[1] > delta.shape[0]:
                delta = np.array(delta).reshape(-1)
        lambhdha = np.divide(delta,np.sqrt(1-np.square(delta)))
        D = np.diag(np.sqrt(1+np.square(lambhdha)))
        Ocor = cov2cor(Omega)
        Psi = np.matmul(D,np.matmul((Ocor-np.outer(delta,delta)),D))
        Psi = (Psi + Psi.T)/2
        O_inv = np.linalg.inv(Omega)
        O_pcor = -cov2cor(O_inv) 
        O_pcor[np.diag_indices(p,ndim=2)] = 1 
        R = Ocor + np.multiply(zeta(2,tau),np.outer(delta,delta))
        R[np.tril_indices(d,k=-1)] = R[np.triu_indices(d,k=1)]
        ratio2 = np.divide(np.square(delta_star),1+np.multiply(zeta(2,tau),np.square(delta_star)))
        gamma1M = np.multiply(np.square(zeta(3,tau)),np.power(ratio2,3)) 
        gamma2M = np.multiply(zeta(4,tau),np.square(ratio2))
        # SN book: see (5.74), (5.75) on p.153
        cp = (beta, Sigma, gamma1, tau, omega, R, O_inv, Ocor, O_pcor, 
              lambhdha, Psi, delta, delta_star, alpha_star, gamma1M, gamma2M)
    return(cp) 
  
  
  
  
  
  
def delta_etc(alpha,*args):
    
    """
    alpha = location paramter
    Scale parameter can be passed as optional argument
    """
    
    largs = len(args)
    if np.isinf(mu).any():
        inf = np.where(np.isinf(np.abs(alpha)))
        inf_flag = True
    else:
        inf_flag = False
        
    if type(alpha)==np.matrix:
        alpha = np.array(alpha)
        
    if len(alpha.shape) > 1: 
        alpha = alpha.reshape(-1)
    
    if(largs == 0): # case d=1
        delta = alpha/np.sqrt(1+np.square(alpha))
        if inf_flag:
            delta[inf] = np.sign(alpha[inf])
        alpha_star = np.nan 
        delta_star = np.nan
        Ocor = np.nan
    else: # d>1
        Omega = args[0]
        if(any(Omega.shape != np.repeat(len(alpha),2))): 
            raise(ValueError("Dimension mismatch"))
        Ocor = cov2cor(Omega)
        if(not(inf_flag)): # d>1, standard case
            Ocor_alpha = np.matmul(Ocor,alpha)
            alpha_sq = np.sum(np.multiply(alpha,Ocor_alpha))
            delta = Ocor_alpha/np.sqrt(1+alpha_sq)
            alpha_star = np.sqrt(alpha_sq)
            delta_star = np.sqrt(alpha_sq/(1+alpha_sq))

        else: # d>1, case with some abs(alpha)=Inf
            if(len(inf) > 1): 
                warnings.warn("Several abs(alpha)==Inf, I handle them as 'equal-rate Inf'") 
            k = np.repeat(0,alpha.shape[0])
            if inf_flag:
                k[inf] = np.sign(alpha[inf])
            Ocor_k = np.matmul(Ocor,k) 
            delta = Ocor_k/np.sqrt(np.sum(np.multiply(k,Ocor_k)))
            delta_star = 1
            alpha_star = np.infty
    return(delta, alpha_star, delta_star, Ocor)
    
     
def cov2cor(Sigma):
    
    """
    Efficient transformation of covariance into correlation matrix
    """
    
    n,p = Sigma.shape
    if (p != n): 
        raise(ValueError("'Sigma' must be a square numeric matrix"))
    Is = np.sqrt(1/np.diag(Sigma))
    if (not(np.isfinite(Is)).any): 
        warnings.warn("diag(.) had 0 or NA entries; non-finite result is doubtful")
    Rho = Sigma
    Rho = np.multiply(np.multiply(Is,Sigma),np.repeat(Is,p).reshape((p,p)))
    Rho[np.diag_indices(p,ndim=2)] = 1
    return(Rho)
    
def force_symmetry(x, tol=10*np.sqrt(np.finfo(float).resolution)): 
    
    if (type(x) not in (np.matrix,np.ndarray)): 
        raise(ValueError("x must be a matrix"))
    err = np.divide(np.abs(x-x.T),(1+np.abs(x)))
    max_err = np.max(np.divide(err,(1+err)))
    if max_err > tol: 
        warnings.warn("matrix seems not to be symmetric")
    if max_err > 100*tol: 
        raise(ValueError("Matrix is not symmetric"))
    return((x + x.T)/2)
    
def zeta(k, x): # k integer in (0,5)
    
    if type(x) == np.matrix:
        x = np.array(x)
        
    if len(x.shape) > 1:
        x = x.reshape(-1)
  
    if(((k<0 or k>5) or not(k == round(k)))): 
        return(None)
        
    na = np.isnan(x)
    if na.any():
        x[na] = 0
    x2 = np.square(x)
    if k==0:
        z = np.log(spp.norm.cdf(x)) + np.log(2)
    if k==1:
        ind_sm_neg_50 = (x <= -50)
        z = x
        if ind_sm_neg_50.any():
            xx = x[ind_sm_neg_50]
            xx2 = x2[ind_sm_neg_50]
            z[ind_sm_neg_50] = -np.divide(xx,1 -np.divide(1,(xx2+2)) +np.divide(1,np.multiply((xx2+2),(xx2+4))) 
                -np.divide(5,np.multiply(np.multiply(xx2+2,xx2+4),(xx2+6)))
                +np.divide(9,np.multiply(np.multiply(np.multiply(xx2+2,xx2+4),xx2+6),xx2+8)) 
                -np.divide(129,np.multiply(np.multiply(np.multiply(np.multiply(xx2+2,xx2+4),xx2+6),xx2+8),xx2+10)))  
            z[not(ind_sm_neg_50)] = np.exp(np.log(spp.norm.pdf(x[not(ind_sm_neg_50)])) - np.log(spp.norm.cdf(x[not(ind_sm_neg_50)])))
        else:
            z = np.exp(np.log(spp.norm.pdf(x)) - np.log(spp.norm.cdf(x)))
    if k==2:
        z = -np.multiply(zeta(1,x),x+zeta(1,x))
    if k==3:
        z = -np.multiply(zeta(2,x),x+zeta(1,x)) - np.multiply(zeta(1,x),1+zeta(2,x))
    if k==4:
        z = -np.multiply(zeta(3,x),x+2*zeta(1,x)) - 2*np.multiply(zeta(2,x),1+zeta(2,x))
    if k==5:
        z = -np.multiply(zeta(4,x),x+2*zeta(1,x)) -np.multiply(zeta(3,x),3+4*zeta(2,x)) \
            -2*np.multiply(zeta(2,x),zeta(3,x))
    
    neg_inf = (x == -np.inf)
    if(neg_inf.any()):
        if k==1:
            z[neg_inf] = np.inf
        if k==2:
            z[neg_inf] = -1
        if k in (3,4,5):
            z[neg_inf] = 0
    
    pos_inf = (x==np.inf)        
    if ((k>1) and pos_inf.any()): 
        z[pos_inf] = 0
        
    return(z)
    
    