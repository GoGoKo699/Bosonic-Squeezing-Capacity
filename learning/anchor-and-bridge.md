# Holevo bridge to random-squeezing capacity

[Project milestones](milestones.md) · [Scientific route](../science/README.md) · [Model and theorem](../science/01-model.md)

The educational anchor is Alexander S. Holevo, **Quantum Systems, Channels, Information: A Mathematical Introduction**, **second revised and expanded edition (2019)**, De Gruyter. [Book DOI](https://doi.org/10.1515/9783110642490) · [Publisher's contents](https://www.degruyterbrill.com/document/doi/10.1515/9783110642490-toc/html).

The book supplies the language of states, channels, entropy, quantum transmission, and constrained bosonic systems. The bridge below connects that language to this project's actual proofs. Chapter numbers and titles follow the selected edition; the route makes no page-level or unverified subsection assignment.

## The physical question

An oscillator passes through a parametric drive with a fixed known squeezing axis. On each use the amount of squeezing is a fresh, unobserved Gaussian random variable. More input photons allow more complicated wavefunctions, but how much additional quantum information survives this particular noise?

Squeezing multiplies position by a positive scale factor. In the coordinate $`y=\ln|x|`$, multiplication becomes translation: the noise shifts the wavefunction along a logarithmic axis. The coherent label of the positive or negative half-line remains a qubit. This sign/parity subsystem is inherited from earlier work; it supplies a useful foothold rather than the growing capacity rate.

The photon Hamiltonian changes under the coordinate transformation. It contains the weights $`e^{2y}`$ and $`e^{-2y}`$. In the lower construction, a logarithmic box of length $`L`$ has a uniform code-energy bound proportional to $`e^L`$. The construction fits a number of orthogonal modes proportional to $`L`$ into that interval while bounding the second moment of the squeezing generator. Their input entropy grows as $`\log_2L`$, and the entropy disclosed to the environment stays bounded.

The converse rules out doing better with other states or collective codes. The environment resolves the squeezing generator into spectral bins of fixed width. A spectral-bin Gibbs inequality and a harmonic Mehler trace bound the receiver entropy that can remain beyond the bin information. The resulting theorem is

```math
Q_\sigma(E)=\log_2\!\ln E+O_\sigma(1),
\qquad E\longrightarrow\infty,
\qquad \sigma>0\ \text{fixed}.
```

Thus the capacity is unbounded, but its increase with the physical photon budget is exceptionally slow.

## A source-to-project map

Use the following chapters as conceptual starting points. Each linked project account supplies the model-specific argument.

| Chapters in the selected anchor | Purpose in this route | Project destination |
| --- | --- | --- |
| **1. Vectors and Operators**; **2. States, Observables, Statistics** | Set up the oscillator state, self-adjoint generator, spectral observables, and trace constraint. | [Channel model](../science/01-model.md) |
| **3. Composite Systems and Entanglement** | Keep the logical register, inaccessible reference, and discarded environment distinct. | [Reference-complete protected qubit](../science/04-protected-qubit.md) |
| **4. Classical Entropy and Information**; **5. The Classical-Quantum Channel** | Interpret the environment as a state ensemble and connect a noisy spectral-bin observation to classical information. | [Environment and spectral bins](../science/03-converse.md#the-environment-resolves-a-unit-width-spectral-bin) |
| **6. Quantum Evolutions and Channels**; **7. Quantum Entropy and Information Quantities** | Use dilation, complementary channels, coherent information, and relative-entropy data processing. | [Achievability](../science/02-achievability.md); [spectral-bin Gibbs inequality](../science/03-converse.md#how-much-entropy-fits-inside-one-spectral-bin) |
| **10. Transmission of Quantum Information**; **11. Channels with Constrained Inputs** | Relate an entropic rate to reliable quantum transmission while retaining the photon budget. | [Operational capacity](../science/01-model.md#operational-capacity); [coding conditions](../science/02-achievability.md#why-the-coding-theorem-applies) |
| **12. Gaussian Systems** | Work with quadratures and Gaussian states, and distinguish a Gaussian unitary from a Gaussian channel. | [Physical Gaussian-input benchmark](../science/05-gaussian-inputs.md) |

Chapters 8–9 concern classical-capacity and entanglement-assisted tasks. They provide comparisons, but this project asks for unassisted quantum transmission.

The logarithmic/Mellin representation, finite log-position code, dilation-spectral heat-trace estimate, and normal log-radius variance argument must be learned from the linked research accounts. They are not attributed to the textbook. The precise energy-constrained coding result used in the proof is Wilde–Qi (2018), identified and checked in [achievability](../science/02-achievability.md#why-the-coding-theorem-applies) and the [references](../references/README.md#wilde-qi-2018).

## Notation to keep separate

The table fixes the project's conventions. The same letters can have other uses in the anchor.

| Project notation | Meaning and distinction |
| --- | --- |
| $`Q,P`$ | Physical oscillator position and momentum, with $`[Q,P]=i`$. |
| $`H=\hat n+\tfrac12`$ | Physical harmonic energy in oscillator units; $`\hat n`$ is the charged photon number. |
| $`E`$ | Allowed mean input photons per use, averaged across a complete block. It is not the environment register. |
| $`G=(QP+PQ)/2`$ | Squeezing generator. It differs from the charged Hamiltonian $`H`$. |
| $`r,\sigma`$ | Realized squeezing amount and its fixed standard deviation. The realized $`r`$ is unobserved. |
| $`y,P_y`$ | Logarithmic position and $`P_y=-i\partial_y`$; under the unitary change of coordinates, $`G`$ becomes $`P_y`$. Physical $`P`$ does not become $`P_y`$. |
| $`L,d`$ | Log-box length and number of radial sine modes. Including both signs gives dimension $`2d`$. |
| $`K`$ in achievability | A positive bound on $`\langle G^2\rangle^{1/2}`$ for the chosen subspace. It is not a hard spectral cutoff. |
| $`K`$ in the converse | The integer spectral-bin label $`\lfloor G\rfloor`$. This is a separate local use of the letter. |
| $`g_2(u)`$ | Thermal oscillator entropy in bits; it is not a spectral value of $`G`$. |
| $`m`$ or $`n`$ as a block index | Number of channel uses. Distinguish this integer from the photon operator $`\hat n`$. |
| $`I_{\rm c}`$ | Coherent information $`S(B)-S(E_{\rm env})`$ for a pure Stinespring environment. |

The two logarithms in the capacity law have different conventions: $`\ln E`$ is natural, while $`\log_2`$ converts a growing effective dimension into qubits.

## Dependencies of the proof

1. **State the communication task before changing coordinates.** The [model](../science/01-model.md) specifies an unknown logical register entangled with a reference, unrestricted encoding and collective decoding, and independent uses of the channel. The unconditional budget is

   ```math
   \mathrm{Tr}\!\left[\rho_{A^m}\sum_{j=1}^m\hat n_j\right]\le mE.
   ```

   This permits correlated inputs, nonuniform energy allocation, and photon-number tails. There is no hard cutoff or Gaussian-input assumption.

2. **Establish the increasing-dimensional lower construction.** In [achievability](../science/02-achievability.md), track normalization, the transformed physical energy, and the generator second moment for every state in the code subspace. The input entropy is $`\log_2(2d)`$; the complementary entropy is bounded by $`g_2(\sigma^2K^2)`$. The coding theorem then turns positive coherent information into asymptotically reliable rates.

3. **Read the converse as an information balance.** In [the upper bound](../science/03-converse.md), the environment already receives most of the spectral-bin information. Relative-entropy data processing bounds what the receiver can retain beyond it. The [Mehler calculation](../science/03-converse.md#the-harmonic-heat-trace-in-the-dilation-spectrum) supplies the logarithmic heat-trace mass that produces the second logarithm. This part covers arbitrary block inputs.

4. **Interpret the Gaussian comparison at its stated scope.** For joint physical Gaussian inputs, including arbitrary correlations across modes, [the benchmark](../science/05-gaussian-inputs.md) proves

   ```math
   I_{\rm c}\!\left(\rho_G^{(m)},\mathcal N_\sigma^{\otimes m}\right)
   \le mB_\sigma,\qquad
   B_\sigma=1+\frac12\log_2\!\left(1+\frac{\pi^2}{8\sigma^2}\right).
   ```

   This bound stays finite as input energy increases, while the explicit non-Gaussian family has unbounded coherent information. The restriction concerns the joint physical input state in that optimization; collective decoding remains unrestricted. It is not a classification of Gaussian hardware.

The [30 project milestones](milestones.md) develop this connected route. Their statements are project-specific; the anchor provides the common mathematical vocabulary.

## Scope of the conclusion

The limiting order matters: hold a positive $`\sigma`$ fixed and then increase $`E`$. The result does not provide a uniform expansion through the zero-noise limit. It gives the leading capacity law and explicit bounds rather than the exact finite-energy optimum.

The channel is lossless in the sense that no attenuator or lost output port is added. Its stochastic drive can supply oscillator energy: $`E_{\rm out}+\tfrac12=e^{2\sigma^2}(E_{\rm in}+\tfrac12)`$. Counting that mean injection preserves the leading law at fixed noise strength, but preparation work, recovery work, and circuit complexity are separate resources.

The exact sign/parity qubit, the arbitrary-code converse, and the Gaussian-input benchmark address different questions. Together they show what survives, how much rate can grow, and why physical Gaussian inputs cannot produce that growth in coherent information. They establish neither an efficient device implementation nor robustness to loss, uncertain squeezing axes, or additional noncommuting noise. The [interpretation](../science/07-interpretation.md) and [related-work account](../science/06-related-work.md) keep these boundaries and inherited ingredients explicit.
