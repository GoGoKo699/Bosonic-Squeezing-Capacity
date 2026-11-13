# References

[Scientific overview](../science/README.md) · [Related-work comparison](../science/06-related-work.md)

The labels below identify the primary scientific sources used in the account. A preprint date and a journal publication date are distinguished when they differ.

## Noise, subsystem and channel comparisons

<a id="sakuldee-tonekaboni"></a>

**[ST24]** Fattah Sakuldee and Behnam Tonekaboni, “Noise decoupling for state transfer in continuous-variable systems,” *Physical Review A* **109**, 032404 (2024). [Published article](https://doi.org/10.1103/PhysRevA.109.032404) · [Accepted manuscript](https://link.aps.org/accepted/10.1103/PhysRevA.109.032404) · [arXiv:2307.02059](https://arxiv.org/abs/2307.02059).

Section IV, especially equations (70)–(72), treats real squeezing and the logarithmic-coordinate convolution; the control model allows interventions along the transmission path. This is an antecedent for the noise and coordinate representation, rather than for the capacity theorem.

<a id="marshall-2019"></a>

**[MJPL19]** Kevin Marshall, Daniel F. V. James, Alexandru Paler and Hoi-Kwan Lau, “Universal quantum computing with thermal state bosonic systems,” *Physical Review A* **99**, 032345 (2019). [Published article](https://doi.org/10.1103/PhysRevA.99.032345) · [Accepted manuscript](https://link.aps.org/accepted/10.1103/PhysRevA.99.032345) · [arXiv:1812.04154v2](https://arxiv.org/abs/1812.04154v2).

Section III and equation (18) define the quadrature-sign parity logical observables. Exact same-axis squeeze protection is an immediate corollary of this prior subsystem. The preprint first appeared in 2018; the journal article is from 2019.

<a id="lau-clerk-2019"></a>

**[LC19]** Hoi-Kwan Lau and Aashish A. Clerk, “High-fidelity bosonic quantum state transfer using imperfect transducers and interference,” *npj Quantum Information* **5**, 31 (2019). [Published article](https://doi.org/10.1038/s41534-019-0143-1) · [arXiv:1812.05666](https://arxiv.org/abs/1812.05666).

The Methods discussion of noiseless-subsystem encoding applies quadrature-sign parity ideas to transduction noise; its transfer architecture and fidelity objective differ from the present capacity problem.

<a id="arqand-2020"></a>

**[AMM20]** Amir Arqand, Laleh Memarzadeh and Stefano Mancini, “Quantum capacity of a bosonic dephasing channel,” *Physical Review A* **102**, 042413 (2020). [Published article](https://doi.org/10.1103/PhysRevA.102.042413) · [arXiv:2007.03897](https://arxiv.org/abs/2007.03897).

This number-dephasing model has a single-letter optimization and finite high-energy capacity limit; it is an important compact-phase comparison.

<a id="lami-wilde-2023"></a>

**[LW23]** Ludovico Lami and Mark M. Wilde, “Exact solution for the quantum and private capacities of bosonic dephasing channels,” *Nature Photonics* **17**, 525–530 (2023). [Published article](https://doi.org/10.1038/s41566-023-01190-4).

The exact unconstrained capacity formula concerns random number rotations and the relative entropy of their phase law to uniform. It does not use the continuous dilation generator with a harmonic photon constraint.

<a id="holevo-2007"></a>

**[H07]** A. S. Holevo, “Single-Mode Quantum Gaussian Channels: Structure and Quantum Capacity,” *Problems of Information Transmission* **43**, 1–11 (2007). [Published article](https://doi.org/10.1134/S0032946007010012) · [arXiv:quant-ph/0607051v2](https://arxiv.org/abs/quant-ph/0607051v2), titled “One-mode quantum Gaussian channels” (2006).

The canonical Gaussian-channel classification clarifies the scope of comparisons with the one-quadrature additive-noise class. The random squeeze mixture is not Gaussian in the original oscillator variables.

<a id="lapidoth-moser-2003"></a>

**[LM03]** Amos Lapidoth and Stefan M. Moser, “Capacity Bounds Via Duality With Applications to Multiple-Antenna Systems on Flat-Fading Channels,” *IEEE Transactions on Information Theory* **49**, 2426–2467 (2003). [Published article](https://doi.org/10.1109/TIT.2003.817449) · [Author-hosted article](https://moser-isi.ethz.ch/docs/papers/alap-smos-2003-3.pdf).

The classical double-logarithmic fading law and logarithmic-amplitude geometry are prior results and provide a useful analogy. They are not quantum coherent-information or quantum-code theorems.

## Entropy and energy-constrained coding

<a id="frank-lieb-2012"></a>

**[FL12]** Rupert L. Frank and Elliott H. Lieb, “Entropy and the Uncertainty Principle,” *Annales Henri Poincaré* **13**, 1711–1717 (2012). [Published article](https://doi.org/10.1007/s00023-012-0175-y) · [arXiv:1109.1209v1](https://arxiv.org/abs/1109.1209v1) (2011).

Theorem 2.1, including the subsequent Fourier-convention remark, gives a related logarithmic-coordinate entropy route. The main converse here instead uses spectral-bin Gibbs data processing and the Mehler trace.

<a id="wilde-qi-2018"></a>

**[WQ18]** Mark M. Wilde and Haoyu Qi, “Energy-constrained private and quantum capacities of quantum channels,” *IEEE Transactions on Information Theory* **64**, 7802–7827 (2018). [Published article](https://doi.org/10.1109/TIT.2018.2854766) · [arXiv:1609.01997v2](https://arxiv.org/abs/1609.01997v2) (final journal version).

Definition 3, Condition 1 and Theorem 5 provide the Gibbs-observable, finite-output-entropy and regularized coherent-information coding framework. The present proof verifies these conditions for the squeeze channel rather than assuming finite-dimensional coding applies without an energy argument.

<a id="wolf-2007"></a>

**[WPGG07]** Michael M. Wolf, David Pérez-García and Géza Giedke, “Quantum Capacities of Bosonic Channels,” *Physical Review Letters* **98**, 130501 (2007). [Published article](https://doi.org/10.1103/PhysRevLett.98.130501) · [arXiv:quant-ph/0606132v1](https://arxiv.org/abs/quant-ph/0606132v1). Gaussian extremality and degradable-channel methods inform the finite-covariance radial-channel bound.

<a id="pav-2015"></a>

**[P15]** Steven E. Pav, “Moments of the log non-central chi-square distribution,” [arXiv:1503.06266v1](https://arxiv.org/abs/1503.06266v1) (2015). Sections 2–3 give the log moments and Poisson-mixture representation used in the normal log-radius variance lemma.

**[DLMF]** NIST Digital Library of Mathematical Functions, [§5.15: Polygamma Functions](https://dlmf.nist.gov/5.15). The half-integer trigamma value and recurrence identities are standard special-function ingredients.

## Related public accounts

These repository links are pinned to source revisions so that the scientific comparison is reproducible. They identify related accounts, not independent validation of this theorem.

| Account and inspected revision | Scientific source used | Relationship |
| --- | --- | --- |
| [Bosonic Phase Noise Capacity](https://github.com/GoGoKo699/Bosonic-Phase-Noise-Capacity/tree/2080352d5c356b3a87d8cc8780b787bc3ca0fc5f) | [Capacity theorem](https://github.com/GoGoKo699/Bosonic-Phase-Noise-Capacity/blob/2080352d5c356b3a87d8cc8780b787bc3ca0fc5f/science/03-capacity.md) | Compact number-phase noise, finite-resolution phase entropy and full mean-energy-tail control. |
| [Bosonic Noise Dimension](https://github.com/GoGoKo699/Bosonic-Noise-Dimension/tree/faf9869b24b32a1cce69a771c49b996d6dcf5d58) | [Converse](https://github.com/GoGoKo699/Bosonic-Noise-Dimension/blob/faf9869b24b32a1cce69a771c49b996d6dcf5d58/science/03-converse.md) · [Related work](https://github.com/GoGoKo699/Bosonic-Noise-Dimension/blob/faf9869b24b32a1cce69a771c49b996d6dcf5d58/science/06-related-work.md) | Weyl-displacement noise, arbitrary-code converses and a different energy-dependent resolution. |

The distinctions between these models, the inherited ingredients and the capacity contribution are explained in the [related-work account](../science/06-related-work.md).
