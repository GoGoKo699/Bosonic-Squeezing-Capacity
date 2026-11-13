# Converse: an unrestricted double-logarithmic upper bound

The environment learns the squeezing generator to a fixed spectral resolution. A harmonic-energy budget limits how much entropy can remain inside one such spectral bin. For the dilation generator, that available entropy grows as the logarithm of a logarithm of the photon budget.

This section proves the upper bound for arbitrary correlated inputs across arbitrarily many independent channel uses. It imposes neither a photon-number cutoff nor a Gaussian restriction on the input, encoder or decoder.

## Statement

Keep the [model conventions](01-model.md):
$`[Q,P]=i`$,
$`H=(Q^2+P^2)/2=N+1/2`$,
$`G=(QP+PQ)/2`$, and

```math
\mathcal N_\sigma(\rho)
=
\int_{\mathbb R}
\frac{e^{-s^2/(2\sigma^2)}}{\sqrt{2\pi}\sigma}
e^{-isG}\rho e^{isG}\,ds,
\qquad \sigma>0.
```

The parameter $`\sigma`$ is fixed. Each channel use draws its own independent, unobserved squeezing parameter. Let $`Q_\sigma(E)`$ denote unassisted quantum capacity with unconditional mean input photon number at most $`E`$ per use, averaged over the whole coding block. Define

```math
\begin{aligned}
h_\sigma(E)&=e^{2\sigma^2}\left(E+\frac12\right),\\
A_\sigma(E)&=\max\{1,h_\sigma(E)\},\\
C_\sigma
&=
\frac12\log_2\!\left[
2\pi e\left(\frac{25}{12}+\frac{1}{2\sigma^2}\right)
\right].
\end{aligned}
```

**Theorem.** For every $`E\ge0`$ and fixed $`\sigma>0`$,

```math
Q_\sigma(E)
\le
C_\sigma+
\log_2\!\left[
\frac{e}{\pi}
\ln\!\bigl(10A_\sigma(E)\bigr)
\right].
```

One may also take the minimum of this expression and the entropy bound $`g(E)`$, where

```math
g(E)=(E+1)\log_2(E+1)-E\log_2E,
\qquad g(0)=0.
```

In particular,

```math
Q_\sigma(E)\le \log_2\ln E+O_\sigma(1)
\qquad (E\longrightarrow\infty).
```

Together with [achievability](02-achievability.md), this gives the matching law with leading coefficient one. The constants above are convenient explicit bounds, not optimal finite-energy constants. This is a capacity converse for vanishing-error communication, not an exponential strong-converse theorem.

## Energy and entropy are finite without a hard cutoff

The self-adjoint dilation generator can be defined directly by its strongly continuous unitary group

```math
(e^{-isG}\psi)(x)=e^{-s/2}\psi(e^{-s}x).
```

The unitary log-coordinate transformation from the [model](01-model.md) identifies $`G`$ with the self-adjoint momentum operator on two copies of $`L^2(\mathbb R)`$. The inverse image of the compactly supported smooth momentum core consists of smooth functions compactly supported away from $`x=0`$ and is contained in the Schwartz space. Thus the Schwartz space is a core for $`G`$. It is also a core for $`H`$, by harmonic-oscillator spectral approximation. The generator $`J=(Q^2-P^2)/2`$ is, up to sign, a harmonic phase rotation of $`G`$; harmonic phase rotations preserve the Schwartz space. These observations give a common invariant core for all three self-adjoint generators. Statements below about unbounded operators use their self-adjoint closures and closed quadratic forms.

For $`J=(Q^2-P^2)/2`$, the ladder-operator identity on the Schwartz core is

```math
\|G\psi\|^2+\|J\psi\|^2
=
\|H\psi\|^2+\frac34\|\psi\|^2.
```

Indeed, $`J=(a^2+a^{\dagger2})/2`$ and
$`G=i(a^{\dagger2}-a^2)/2`$, so

```math
J^2+G^2
=
\frac{a^2a^{\dagger2}+a^{\dagger2}a^2}{2}
=
N^2+N+1
=
H^2+\frac34.
```

Approximation in the graph norm of $`H`$ extends the norm identity to $`\mathrm{Dom}H`$. Since $`G`$ and $`J`$ are closed, it also gives
$`\mathrm{Dom}H\subseteq\mathrm{Dom}G\cap\mathrm{Dom}J`$.
Consequently

```math
G^2\le H^2+\frac34
```

as an inequality of closed nonnegative quadratic forms. Applying the operator-monotonicity of the square root gives

```math
|G|
\le
\sqrt{H^2+\frac34}
\le H+\frac12.
```

The last inequality is scalar functional calculus for $`H\ge1/2`$:
$`(h+1/2)^2\ge h^2+3/4`$ for $`h\ge1/2`$.
The argument uses a form inequality and square-root monotonicity; it does not assume that $`H`$ and $`G`$ commute. For completeness, square-root monotonicity also holds for unbounded positive operators ordered as forms: resolvent order and the positive integral $`\sqrt A=\pi^{-1}\int_0^\infty t^{-1/2}A(A+t)^{-1}\,dt`$ give the result by monotone form integration.

Thus every finite-energy state has finite first absolute moment of the spectral observable $`G`$. The integer-valued observable

```math
K=\lfloor G\rfloor,
\qquad
P_j=\mathbf 1_{[j,j+1)}(G),
\quad j\in\mathbb Z,
```

has finite first absolute moment as well. Its Shannon entropy is finite: comparison with the normalized distribution proportional to $`2^{-|j|}`$ gives an elementary finite bound in terms of that moment. The same statement applies to the joint spectral bins of finitely many modes.

Squeezing rescales the quadratures reciprocally. Gaussian averaging gives the exact energy identity

```math
\mathrm{Tr}\!\left[H\mathcal N_\sigma(\rho)\right]
=
e^{2\sigma^2}\mathrm{Tr}[H\rho].
```

It holds first on the common core and then at every finite harmonic energy by positive quadratic-form approximation. In particular, a block input $`\rho_{A^n}`$ satisfying

```math
\mathrm{Tr}\!\left[
\rho_{A^n}\sum_{i=1}^nN_i
\right]\le nE
```

has output $`\omega_{B^n}=\mathcal N_\sigma^{\otimes n}(\rho_{A^n})`$ with

```math
\mathrm{Tr}\!\left[
\omega_{B^n}\sum_{i=1}^nH_i
\right]\le nh_\sigma(E).
```

The harmonic Gibbs bound makes both input and output entropies finite. If $`R`$ purifies the input and a pure environment is used, then

```math
S(E^n)=S(RB^n)\le S(R)+S(B^n)<\infty.
```

The complementary entropy is therefore finite even when the input has infinite second moment of $`G`$. No second-moment assumption on the input is needed here.

These facts also verify the Gibbs-observable and finite-output-entropy conditions of the general [energy-constrained coding theorem](../references/README.md#wilde-qi-2018).

## The environment resolves a unit-width spectral bin

Use a vacuum oscillator as the environment and the dilation

```math
V_\sigma
=
\exp\!\left[-i\sqrt2\,\sigma G\otimes q_{\rm e}\right].
```

The vacuum $`q_{\rm e}`$ distribution has variance $`1/2`$, so tracing out the environment gives precisely $`\mathcal N_\sigma`$. For spectral value $`u`$ of $`G`$, the environmental output is the coherent state $`|-i\sigma u\rangle`$. Thus

```math
\mathcal N_\sigma^{\,c}(\rho)
=
\int_{\mathbb R}
\langle E_G(du)\rangle_\rho\,
|-i\sigma u\rangle\langle-i\sigma u|.
```

This is an operator-valued spectral integral; it does not require normalizable eigenvectors of $`G`$.

Environmental momentum homodyne, rescaled by $`-1/(\sqrt2\,\sigma)`$, realizes the classical channel

```math
Y=U+Z,
\qquad
Z\sim\mathcal N\!\left(0,\frac{1}{4\sigma^2}\right),
```

where $`U`$ has the input spectral distribution of $`G`$ and $`Z`$ is independent of it. Put $`K=\lfloor U\rfloor`$ and $`D=K-\lfloor Y\rfloor`$. Since

```math
|D|\le |Z|+1,
\qquad
\mathbb E D^2\le 2\mathbb E Z^2+2,
```

the discrete-entropy bound obtained by adding an independent uniform random variable on $`[-1/2,1/2]`$ gives

```math
H(D)
\le
\frac12\log_2\!\left[
2\pi e\left(
2+\frac{1}{2\sigma^2}+\frac1{12}
\right)
\right]
=
C_\sigma.
```

Given $`Y`$, the variables $`D`$ and $`K`$ determine one another. Hence

```math
H(K\mid Y)=H(D\mid Y)\le H(D)\le C_\sigma.
```

Apply the Holevo bound to the discrete ensemble obtained by grouping the coherent environmental states into the bins of $`U`$. It yields

```math
S(E)\ge I(K;Y)\ge H(K)-C_\sigma.
```

For a correlated $`n`$-mode input, the environment contains the corresponding correlated mixture of product coherent states. Product homodyne measurements produce $`Y^n=U^n+Z^n`$ with independent Gaussian measurement noises. The input coordinates $`U_i`$ need not be independent. Conditional entropy and subadditivity give

```math
\begin{aligned}
H(K^n\mid Y^n)
&=H(D^n\mid Y^n)\\
&\le H(D^n)
\le \sum_{i=1}^nH(D_i)
\le nC_\sigma.
\end{aligned}
```

Therefore

```math
S(E^n)\ge H(K^n)-nC_\sigma.
```

The channel preserves the joint spectral distribution of $`G_1,\ldots,G_n`$, so $`H(K^n)`$ is the same whether evaluated on the input or output.

## How much entropy fits inside one spectral bin?

For $`\beta>0`$, let

```math
Z_\beta=\mathrm{Tr}e^{-\beta H}
=\frac{1}{2\sinh(\beta/2)},
\qquad
\gamma_\beta=\frac{e^{-\beta H}}{Z_\beta},
\qquad
B_\beta=\sup_{j\in\mathbb Z}
\mathrm{Tr}\!\left[P_je^{-\beta H}\right].
```

**Spectral-bin Gibbs inequality.** For every finite-energy $`n`$-mode state $`\omega`$,

```math
S(\omega)-H(K^n)_\omega
\le
\frac{\beta}{\ln2}
\mathrm{Tr}\!\left[\omega\sum_{i=1}^nH_i\right]
+n\log_2B_\beta.
```

Apply relative-entropy data processing to the measurement of the joint projectors $`P_{j_1}\otimes\cdots\otimes P_{j_n}`$ and the reference state $`\gamma_\beta^{\otimes n}`$. If $`p_{\boldsymbol j}`$ is the measured distribution of $`\omega`$ and $`q_j=\mathrm{Tr}[P_j\gamma_\beta]`$, then

```math
\begin{aligned}
&-S(\omega)
+\frac{\beta}{\ln2}
\mathrm{Tr}\!\left[\omega\sum_iH_i\right]
+n\log_2Z_\beta\\
&\hspace{1cm}\ge
-H(p)-\sum_{\boldsymbol j}
p_{\boldsymbol j}\log_2\!\left(\prod_iq_{j_i}\right).
\end{aligned}
```

Rearranging and using
$`Z_\beta q_j=\mathrm{Tr}[P_je^{-\beta H}]\le B_\beta`$
proves the claim. The entropy and cross-entropy expressions are well defined: quantum relative entropy is finite at finite harmonic energy, data processing bounds its measured counterpart, and spectral-bin entropy is finite by the preceding form bound.

Using the full harmonic partition function in this estimate would give only an order-$`\log E`$ converse. The heat-trace mass inside one fixed generator bin is much smaller.

## The harmonic heat trace in the dilation spectrum

The exact characteristic function of the finite positive spectral measure
$`\nu_\beta(du)=\mathrm{Tr}[e^{-\beta H}E_G(du)]`$ is

```math
F_\beta(t)
=
\mathrm{Tr}\!\left[e^{-\beta H}e^{itG}\right]
=
\frac{1}{\sqrt{2(\cosh\beta\cosh t-1)}}.
```

Derive it directly from the harmonic Mehler kernel,

```math
K_\beta(x,y)
=
\frac{1}{\sqrt{2\pi\sinh\beta}}
\exp\!\left[
-\frac{(x^2+y^2)\cosh\beta-2xy}{2\sinh\beta}
\right].
```

Inserting the coordinate action of squeezing in the trace reduces it to the convergent Gaussian integral

```math
\mathrm{Tr}[e^{-\beta H}e^{-itG}]
=
e^{t/2}\int_{\mathbb R}K_\beta(x,e^tx)\,dx
=
\frac{1}{\sqrt{2(\cosh\beta\cosh t-1)}}.
```

The formula is even in $`t`$, so the sign convention in the characteristic function does not change it. It includes both sign sectors and reduces to $`Z_\beta`$ at $`t=0`$.

For every fixed $`\beta>0`$, $`F_\beta`$ is integrable. Fourier inversion gives a bounded continuous density of $`\nu_\beta`$,

```math
h_\beta(u)=
\frac{1}{2\pi}\int_{\mathbb R}e^{-itu}F_\beta(t)\,dt,
\qquad
\sup_uh_\beta(u)
\le\frac{1}{2\pi}\int_{\mathbb R}F_\beta(t)\,dt.
```

Each bin has width one, so $`B_\beta\le\sup_uh_\beta(u)`$. For $`0<\beta\le1`$,

```math
\begin{aligned}
F_\beta(t)&\le\frac{1}{\sqrt{\beta^2+t^2}},
&& |t|\le1,\\
F_\beta(t)&\le\frac{1}{2\sinh(|t|/2)},
&& |t|\ge1.
\end{aligned}
```

The first estimate follows from
$`\cosh\beta\cosh t-1\ge(\beta^2+t^2)/2`$;
the second uses $`\cosh\beta\ge1`$. Consequently,

```math
\begin{aligned}
B_\beta
&\le
\frac1\pi
\left[
\mathrm{arsinh}\!\left(\frac1\beta\right)
-\ln\tanh\!\left(\frac14\right)
\right]\\
&\le\frac1\pi\ln\!\left(\frac{c_*}{\beta}\right)
\le\frac1\pi\ln\!\left(\frac{10}{\beta}\right),
\\
c_*&=(1+\sqrt2)\coth(1/4)<10.
\end{aligned}
```

A fixed-width interval in the dilation spectrum therefore has harmonic heat-trace mass only of order $`\ln(1/\beta)`$. This is the source of the double logarithm.

## Complete the block converse

Let $`\rho_{A^n}`$ be any correlated admissible input, $`\omega_{B^n}`$ its output and $`E^n`$ the complementary output. Combine the entropy inequalities:

```math
\begin{aligned}
I_{\rm c}\!\left(\rho_{A^n},\mathcal N_\sigma^{\otimes n}\right)
&=S(B^n)-S(E^n)\\
&\le S(B^n)-H(K^n)+nC_\sigma\\
&\le n\left[
\frac{\beta h_\sigma(E)}{\ln2}
+\log_2B_\beta+C_\sigma
\right].
\end{aligned}
```

Choose $`\beta=1/A_\sigma(E)\in(0,1]`$. Then
$`\beta h_\sigma(E)\le1`$ and

```math
\begin{aligned}
\frac1nI_{\rm c}
&\le\frac1{\ln2}
+\log_2\!\left[
\frac1\pi\ln\!\bigl(10A_\sigma(E)\bigr)
\right]+C_\sigma\\
&=
C_\sigma+
\log_2\!\left[
\frac e\pi\ln\!\bigl(10A_\sigma(E)\bigr)
\right].
\end{aligned}
```

The bound is independent of $`n`$. The general energy-constrained capacity theorem gives the announced upper bound after optimization over all inputs and regularization. The elementary bound
$`I_{\rm c}\le S(\rho_{A^n})\le ng(E)`$
gives the optional minimum with $`g(E)`$.

For fixed $`\sigma>0`$,
$`\ln A_\sigma(E)=\ln E+2\sigma^2+o(1)`$.
The upper bound is thus $`\log_2\ln E+O_\sigma(1)`$, matching the lower bound. No assumption about Gaussian optimizers, additivity of coherent information or degradability enters the argument.

## Scope and verification

The spectral-bin measurement and environmental homodyne are mathematical tools in the converse; these measurements are not supplied to the communicating parties. The bound charges unconditional input mean energy and permits its arbitrary redistribution across a coding block. Finite output energy follows from the channel itself.

The Gaussian squeezing law enters in two precise places: finite exponential moments give the output-energy factor, and the vacuum dilation lets the environment resolve $`G`$ with constant Gaussian measurement noise. A different law needs corresponding estimates. The constants are not uniform as $`\sigma\to0`$. Added loss, an unknown squeezing axis and in-channel interventions are outside this theorem.

The [heat-trace verification program](../verification/heat_trace.py) compares the Mehler normalization with finite Fock matrices and checks the explicit integral majorant at selected inverse temperatures. Those computations support conventions and selected finite calculations. The unrestricted converse is the analytical argument above.

