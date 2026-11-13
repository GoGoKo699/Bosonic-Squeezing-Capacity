# Thirty milestones

[Learning route](README.md) · [Selected anchor and bridge](anchor-and-bridge.md) · [Scientific route](../science/README.md)

This is the project's common milestone map. It develops the operator, entropy and coding background first, then follows the scientific argument from the channel to its full resource conclusion. The only educational anchor is A. S. Holevo, *Quantum Systems, Channels, Information: A Mathematical Introduction*, second revised and expanded edition (2019), [DOI](https://doi.org/10.1515/9783110642490). Chapter pointers below use that edition; the bridge identifies the additional research sources.

Phase I contains twelve background milestones. Phase II contains eighteen narrative milestones, ending with a synthesis of the achievable code, unrestricted converse, Gaussian-input comparison and physical scope. Each entry specifies six fields; dependencies describe the scientific order rather than an individual learner's progress.

## Phase I — Background and preliminaries

### M01 — The oscillator as a quantum system

- **ID / phase:** M01 · Phase I.
- **Central question:** Which operators describe the information carrier and its charged energy?
- **Understanding target:** Identify the oscillator Hilbert space, position, momentum, number operator and harmonic Hamiltonian, with $`[Q,P]=iI`$ and $`H=\hat n+\tfrac12`$.
- **Dependencies / story role:** Entry point; fixes the physical system before introducing its noise or communication task.
- **Conceptual connection:** A coordinate description and a physical resource observable are separate choices.
- **Source pointers:** Holevo Chapters 1–2; [anchor bridge](anchor-and-bridge.md); [channel conventions](../science/01-model.md#channel-and-conventions).

### M02 — States, mixtures and information

- **ID / phase:** M02 · Phase I.
- **Central question:** How does a density operator represent both coherent superposition and classical uncertainty?
- **Understanding target:** Distinguish pure states, mixed states, ensembles, support and expectation values; recognize that an ensemble is not a unique decomposition of its density operator.
- **Dependencies / story role:** Uses M01 and supplies the language for random squeezing and the maximally mixed code input.
- **Conceptual connection:** Averaging unknown transformations changes a state even when every realized transformation is unitary.
- **Source pointers:** Holevo Chapter 2; [anchor bridge](anchor-and-bridge.md); [random-unitary channel](../science/01-model.md#channel-and-conventions).

### M03 — Channels and random transformations

- **ID / phase:** M03 · Phase I.
- **Central question:** What makes a transformation valid when the input can be entangled with another system?
- **Understanding target:** Understand complete positivity and trace preservation, unitary channels, mixtures of channels, composition and independent tensor-product uses.
- **Dependencies / story role:** Builds on M02; explains why averaging the squeeze unitaries defines a quantum channel.
- **Conceptual connection:** An unobserved random parameter is part of the channel, whereas a revealed parameter would be side information and a different task.
- **Source pointers:** Holevo Chapters 3 and 6; [anchor bridge](anchor-and-bridge.md); [channel definition](../science/01-model.md#channel-and-conventions).

### M04 — A quantum message includes its reference

- **ID / phase:** M04 · Phase I.
- **Central question:** Why is preserving a classical label weaker than transmitting a qubit?
- **Understanding target:** Use composite systems, purification, partial trace and entanglement fidelity to express preservation of arbitrary coherence and entanglement with an inaccessible reference.
- **Dependencies / story role:** Uses M02–M03; fixes the success criterion shared by the capacity theorem and exact protected-qubit example.
- **Conceptual connection:** A sign degree of freedom can be a coherent subsystem rather than a classical flag.
- **Source pointers:** Holevo Chapters 3 and 10; [anchor bridge](anchor-and-bridge.md); [operational capacity](../science/01-model.md#operational-capacity).

### M05 — The receiver and the environment

- **ID / phase:** M05 · Phase I.
- **Central question:** How can a channel be represented by a reversible interaction with an environment?
- **Understanding target:** Relate an isometric dilation to its main and complementary channels; understand that different equivalent environment representations do not give extra access to the receiver.
- **Dependencies / story role:** Extends M03–M04; prepares the two-sided entropy comparison used throughout the proof.
- **Conceptual connection:** Noise can be analyzed through information available to the discarded environment without measuring that environment in the communication protocol.
- **Source pointers:** Holevo Chapters 3 and 6; [anchor bridge](anchor-and-bridge.md); [logarithmic position and the environment](../science/01-model.md#logarithmic-position-and-the-environment).

### M06 — Classical uncertainty at finite resolution

- **ID / phase:** M06 · Phase I.
- **Central question:** How does coarse measurement turn a continuous variable into a finite-resolution information quantity?
- **Understanding target:** Distinguish Shannon entropy, conditional entropy, mutual information and differential entropy; follow binning of a real spectral variable and the role of an added measurement noise.
- **Dependencies / story role:** Uses M02 and supplies the classical part of the environment-resolution converse.
- **Conceptual connection:** A continuous variable need not be learned exactly for its coarse information to limit quantum transmission.
- **Source pointers:** Holevo Chapters 4–5; [anchor bridge](anchor-and-bridge.md); [environmental spectral resolution](../science/03-converse.md#the-environment-resolves-a-unit-width-spectral-bin).

### M07 — Quantum entropy and coherent information

- **ID / phase:** M07 · Phase I.
- **Central question:** Which entropy difference measures a channel's ability to preserve quantum information?
- **Understanding target:** Understand von Neumann entropy, concavity, subadditivity, relative entropy and data processing, then interpret coherent information as receiver entropy minus complementary-output entropy.
- **Dependencies / story role:** Combines M04–M06; supplies the quantity bounded below by the code construction and above for arbitrary inputs.
- **Conceptual connection:** Increasing receiver entropy alone is insufficient when the environment learns the same information.
- **Source pointers:** Holevo Chapters 7 and 10; [anchor bridge](anchor-and-bridge.md); [receiver entropy and coherent information](../science/02-achievability.md#4-receiver-entropy-and-coherent-information).

### M08 — Mean energy and Gibbs entropy bounds

- **ID / phase:** M08 · Phase I.
- **Central question:** What does a mean photon budget control in an infinite-dimensional system?
- **Understanding target:** Distinguish a mean constraint from a hard photon cutoff; understand the harmonic partition function and the thermal maximum-entropy bound at fixed mean excitation.
- **Dependencies / story role:** Uses M01 and M07; prepares finite-entropy arguments that retain the entire input-energy tail.
- **Conceptual connection:** Rare high-energy components are allowed and must be covered by a converse rather than silently removed.
- **Source pointers:** Holevo Chapters 7 and 11; [anchor bridge](anchor-and-bridge.md); [energy and entropy without a cutoff](../science/03-converse.md#energy-and-entropy-are-finite-without-a-hard-cutoff).

### M09 — Gaussian states and Gaussian operations

- **ID / phase:** M09 · Phase I.
- **Central question:** Why can a mixture of Gaussian unitaries define a non-Gaussian channel?
- **Understanding target:** Identify Gaussian states through their quadrature statistics and covariance matrices; distinguish a Gaussian unitary, a Gaussian channel and a general mixture of Gaussian transformations.
- **Dependencies / story role:** Builds on M01–M03 and M08; prevents applying a Gaussian-channel optimization to the wrong physical channel.
- **Conceptual connection:** The family of allowed physical input states is different from the set of components used by a laboratory circuit.
- **Source pointers:** Holevo Chapter 12; [anchor bridge](anchor-and-bridge.md); [vacuum moment diagnostic](../science/01-model.md#channel-and-conventions); [Gaussian-input statement](../science/05-gaussian-inputs.md#a-bound-independent-of-input-energy).

### M10 — Generators, domains and finite form energy

- **ID / phase:** M10 · Phase I.
- **Central question:** How can finite-energy wavefunctions be used without assuming they are smooth eigenstates?
- **Understanding target:** Understand self-adjoint generators, their unitary groups, spectral measures and quadratic-form energy; distinguish these notions from formal differential expressions or normalizable eigenvectors.
- **Dependencies / story role:** Uses M01 and M08; makes the log-box modes, half-line qubit and unbounded-generator converse mathematically meaningful.
- **Conceptual connection:** A wavefunction can have finite kinetic form energy even when its derivative changes at a boundary.
- **Source pointers:** Holevo Chapter 1; [anchor bridge](anchor-and-bridge.md); [converse domain argument](../science/03-converse.md#energy-and-entropy-are-finite-without-a-hard-cutoff); [subspace energy calculation](../science/02-achievability.md#2-the-physical-energy-bound-holds-on-the-whole-subspace).

### M11 — Fourier representations and spectral resolution

- **ID / phase:** M11 · Phase I.
- **Central question:** How does translation in one coordinate become dephasing in its conjugate spectral variable?
- **Understanding target:** Relate a translation generator to its Fourier representation; understand characteristic functions, fixed-width spectral bins and the difference between a coordinate change and a change of physical energy.
- **Dependencies / story role:** Connects M05–M06 and M10; prepares the common representation behind achievability and the converse.
- **Conceptual connection:** The same noise can look additive in a transformed coordinate while retaining a nonstandard resource cost.
- **Source pointers:** Holevo Chapters 1 and 12; [anchor bridge](anchor-and-bridge.md); [logarithmic representation](../science/01-model.md#logarithmic-position-and-the-environment).

### M12 — From a state calculation to capacity

- **ID / phase:** M12 · Phase I.
- **Central question:** What must be proved before coherent information becomes an operational communication rate?
- **Understanding target:** Understand asymptotic coding, regularization over block inputs, the unconditional mean-energy constraint, and the Gibbs/finite-output-entropy hypotheses of the constrained coding theorem.
- **Dependencies / story role:** Synthesizes M01–M11 into the complete communication framework before the project-specific argument begins.
- **Conceptual connection:** One useful input gives an achievable lower bound; an unrestricted capacity law also needs an upper bound covering every admissible block code.
- **Source pointers:** Holevo Chapters 10–11; [anchor bridge](anchor-and-bridge.md); [capacity definition](../science/01-model.md#operational-capacity); [coding conditions](../science/02-achievability.md#why-the-coding-theorem-applies).

## Phase II — Narrative and innovation

### M13 — Fix the operational question

- **ID / phase:** M13 · Phase II.
- **Central question:** Exactly what communication task does the squeezing-capacity theorem answer?
- **Understanding target:** State the known fixed axis, independent unobserved Gaussian squeeze draws, fixed positive variance, lossless channel, absence of control inside a use, and arbitrary encoding/collective decoding under block-averaged input energy.
- **Dependencies / story role:** Uses M12; establishes the quantifiers and resources that every subsequent claim retains.
- **Conceptual connection:** Correlated noise, a revealed squeeze record, intermediate cancellation and additional loss define different channels.
- **Source pointers:** [Model and operational capacity](../science/01-model.md); Holevo Chapters 6, 10–11 through the [anchor bridge](anchor-and-bridge.md).

### M14 — Expose translation and the coherent sign

- **ID / phase:** M14 · Phase II.
- **Central question:** What does the logarithmic position transformation reveal about same-axis squeezing?
- **Understanding target:** Follow the norm-preserving map to log position and a two-dimensional sign factor; identify the transformed generator as radial momentum and the channel as translation noise tensored with a logical identity.
- **Dependencies / story role:** Uses M10–M11 and M13; gives the representation used by all three scientific results.
- **Conceptual connection:** A change of representation reveals a protected subsystem without granting an extra physical communication register.
- **Source pointers:** [Logarithmic representation](../science/01-model.md#logarithmic-position-and-the-environment); [logical factorization](../science/04-protected-qubit.md#logical-observables-and-the-factorization); [prior coordinate mechanism](../science/06-related-work.md#random-squeezing-and-logarithmic-coordinates); [anchor bridge](anchor-and-bridge.md).

### M15 — Recover the inherited qubit exactly

- **ID / phase:** M15 · Phase II.
- **Central question:** Why does preserving sign and parity protect a qubit rather than only a classical bit?
- **Understanding target:** Relate the anticommuting bounded sign/parity observables to the prior QSP encoding; follow the encoder and gauge-tracing decoder, including an external reference and the explicit one-photon half-line example.
- **Dependencies / story role:** Uses M04 and M14; supplies a finite-energy foothold while keeping its prior ownership separate from the growing capacity law.
- **Conceptual connection:** A logical subsystem can be unchanged while its gauge state and physical energy change.
- **Source pointers:** [Protected-qubit account](../science/04-protected-qubit.md); [attribution](../science/06-related-work.md#the-protected-qubit-is-inherited); Holevo Chapters 3, 6 and 10 through the [anchor bridge](anchor-and-bridge.md).

### M16 — Transform the charged Hamiltonian too

- **ID / phase:** M16 · Phase II.
- **Central question:** Why does ordinary translation-channel intuition not give the physical-energy capacity here?
- **Understanding target:** Follow both terms of the transformed oscillator energy, with weights $`e^{2y}`$ and $`e^{-2y}`$; understand why an interval of log-position length proportional to $`\ln E`$ is the natural finite-bandwidth resource.
- **Dependencies / story role:** Combines M08 and M14; identifies the physical mechanism responsible for the second logarithm.
- **Conceptual connection:** Unitary equivalence preserves channel action but does not preserve a specified resource observable unless that observable is transformed as well.
- **Source pointers:** [Physical log-coordinate energy](../science/01-model.md#logarithmic-position-and-the-environment); [energy geometry](../science/07-interpretation.md#a-scale-coordinate-changes-the-energy-geometry); [anchor bridge](anchor-and-bridge.md).

### M17 — Build a growing finite-energy subspace

- **ID / phase:** M17 · Phase II.
- **Central question:** How can increasingly many orthogonal inputs fit within the photon budget while their generator bandwidth stays bounded?
- **Understanding target:** Construct the finite log-position box and its Dirichlet sine modes, count both sign sectors, and verify that the energy and derivative-form bounds hold for every superposition in the code subspace.
- **Dependencies / story role:** Uses M10 and M16; provides the explicit input family required for an achievable rate.
- **Conceptual connection:** The sine modes are interval Laplacian modes extended by zero, not normalizable eigenstates of full-line momentum.
- **Source pointers:** [Logarithmic box and modes](../science/02-achievability.md#1-the-logarithmic-box-and-its-modes); [whole-subspace energy bound](../science/02-achievability.md#2-the-physical-energy-bound-holds-on-the-whole-subspace); [finite-box checks](../verification/log_box.py); [anchor bridge](anchor-and-bridge.md).

### M18 — Keep the environment entropy bounded

- **ID / phase:** M18 · Phase II.
- **Central question:** Why does the environment not learn the growing number of box modes?
- **Understanding target:** Use the coherent-state complementary ensemble and the bounded generator second moment to bound environment excitation and entropy independently of the box length; combine this with entropy concavity at the receiver.
- **Dependencies / story role:** Combines M05, M07–M08 and M17; derives the finite-energy coherent-information lower bound.
- **Conceptual connection:** The receiver's increasing input entropy and the environment's bounded entropy have different dependences on the same code construction.
- **Source pointers:** [Environmental entropy bound](../science/02-achievability.md#3-the-environment-entropy-is-bounded-independently-of-the-box-length); [coherent-information calculation](../science/02-achievability.md#4-receiver-entropy-and-coherent-information); Holevo Chapters 7 and 10 through the [anchor bridge](anchor-and-bridge.md).

### M19 — Obtain an operational growing rate

- **ID / phase:** M19 · Phase II.
- **Central question:** Which part of the lower calculation proves reliable communication at double-logarithmic rate?
- **Understanding target:** Verify the coding hypotheses and then take the high-energy limit at fixed noise and fixed generator bandwidth to obtain $`Q_\sigma(E)\ge\log_2\ln E-O_\sigma(1)`$.
- **Dependencies / story role:** Uses M12 and M18; completes achievability while leaving optimality to the converse.
- **Conceptual connection:** An explicit input subspace and an asymptotic existence theorem do not yet give an efficient encoder or a finite-block error estimate.
- **Source pointers:** [Coding hypotheses](../science/02-achievability.md#why-the-coding-theorem-applies); [large-energy lower bound](../science/02-achievability.md#large-energy-consequence); [anchor bridge](anchor-and-bridge.md).

### M20 — Close the high-frequency escape route

- **ID / phase:** M20 · Phase II.
- **Central question:** Why cannot a different input hide arbitrarily much information in widely separated generator values?
- **Understanding target:** Follow environmental homodyne as a mathematical observation of the generator plus fixed Gaussian noise; bound the conditional entropy of its integer bin by an input-independent constant, including correlated block inputs.
- **Dependencies / story role:** Uses M05–M07, M11 and M14; begins the converse by identifying what is also available to the environment.
- **Conceptual connection:** The homodyne measurement is a converse tool, not side information supplied to either communicating party.
- **Source pointers:** [Environment resolves a spectral bin](../science/03-converse.md#the-environment-resolves-a-unit-width-spectral-bin); Holevo Chapters 4–7 through the [anchor bridge](anchor-and-bridge.md).

### M21 — Retain every allowed energy tail

- **ID / phase:** M21 · Phase II.
- **Central question:** How is the converse defined for arbitrary finite-mean-energy inputs, including those with infinite generator variance?
- **Understanding target:** Use the common-core quadratic-form identity and square-root monotonicity to control the first absolute generator moment; establish finite bin entropy and finite input, receiver and complementary entropies without imposing a hard cutoff.
- **Dependencies / story role:** Uses M08, M10 and M20; makes the unrestricted entropy manipulations legitimate.
- **Conceptual connection:** The lower construction has bounded generator variance, but the converse must not impose that convenient property on every code.
- **Source pointers:** [Energy and entropy domains](../science/03-converse.md#energy-and-entropy-are-finite-without-a-hard-cutoff); [operational mean budget](../science/01-model.md#operational-capacity); [anchor bridge](anchor-and-bridge.md).

### M22 — Bound entropy left inside a bin

- **ID / phase:** M22 · Phase II.
- **Central question:** How much receiver entropy can remain after the generator-bin information is subtracted?
- **Understanding target:** Apply relative-entropy data processing to the joint spectral-bin measurement and a product harmonic Gibbs reference; derive the spectral-bin Gibbs inequality with one common inverse temperature for an arbitrary block.
- **Dependencies / story role:** Combines M07–M08 and M20–M21; reduces all-code optimality to one heat-trace mass rather than assuming independent inputs or equal per-mode energies.
- **Conceptual connection:** A product reference state can bound a correlated input without replacing that input by a product state.
- **Source pointers:** [Spectral-bin Gibbs inequality](../science/03-converse.md#how-much-entropy-fits-inside-one-spectral-bin); Holevo Chapters 7 and 11 through the [anchor bridge](anchor-and-bridge.md).

### M23 — Compute the relevant spectral volume

- **ID / phase:** M23 · Phase II.
- **Central question:** Why is the harmonic heat-trace mass of a fixed generator bin only logarithmic in inverse temperature?
- **Understanding target:** Insert the squeeze action into the Mehler-kernel trace, recover the harmonic partition function at zero argument, and use Fourier inversion plus the explicit integral majorant to bound every unit-width bin.
- **Dependencies / story role:** Uses M01, M10–M11 and M22; supplies the problem-specific estimate that strengthens a logarithmic-energy converse to a double-logarithmic one.
- **Conceptual connection:** The full partition function counts too much; the relevant quantity is its mass within the noise-resolved spectral region.
- **Source pointers:** [Harmonic heat trace](../science/03-converse.md#the-harmonic-heat-trace-in-the-dilation-spectrum); [finite heat-trace checks](../verification/heat_trace.py); [anchor bridge](anchor-and-bridge.md).

### M24 — Match the unrestricted upper and lower laws

- **ID / phase:** M24 · Phase II.
- **Central question:** What prevents arbitrary correlated coding and energy redistribution from improving the leading coefficient?
- **Understanding target:** Combine environmental resolution, the spectral-bin Gibbs inequality, the heat-trace bound and the output-energy identity; optimize the inverse temperature and regularize uniformly over every blocklength.
- **Dependencies / story role:** Synthesizes M19–M23 to establish $`Q_\sigma(E)=\log_2\ln E+O_\sigma(1)`$ for the actual mean-budget task.
- **Conceptual connection:** Matching attainable and universal rates is stronger than a favorable scaling for one code family; it remains a vanishing-error capacity law, not a strong-converse exponent.
- **Source pointers:** [Complete block converse](../science/03-converse.md#complete-the-block-converse); [principal result](../science/01-model.md#principal-result); [anchor bridge](anchor-and-bridge.md).

### M25 — Find the Gaussian log-radius restriction

- **ID / phase:** M25 · Phase II.
- **Central question:** What remains bounded in log position for every physical Gaussian input, even at unbounded photon energy?
- **Understanding target:** Relate a normal quadrature marginal to its logarithmic absolute value; follow the noncentral chi-square/Poisson mixture and the covariance monotonicity proof of the uniform variance bound.
- **Dependencies / story role:** Uses M06, M09 and M14; identifies the geometric restriction behind the Gaussian-input benchmark.
- **Conceptual connection:** Large displacement or squeezing can move a log-radius distribution without giving it arbitrarily large centered variance.
- **Source pointers:** [Log-radius variance lemma](../science/05-gaussian-inputs.md#the-log-radius-variance-of-a-normal-variable); Holevo Chapters 4 and 12 through the [anchor bridge](anchor-and-bridge.md).

### M26 — Use the radial Gaussian-channel tool correctly

- **ID / phase:** M26 · Phase II.
- **Central question:** Where is Gaussian coherent-information optimization valid in this non-Gaussian physical-channel problem?
- **Understanding target:** Establish the finite-covariance bound for the auxiliary translation channel using its degrading map, Gaussian entropy extremality at matching covariance, and the explicit symplectic-eigenvalue calculation.
- **Dependencies / story role:** Combines M05, M07, M09, M14 and M25; bounds radial coherent information without assuming Gaussian optimality for the original squeeze channel.
- **Conceptual connection:** A Gaussian-channel result can be a valid intermediate tool while its standard oscillator energy constraint cannot be transferred to the physical task.
- **Source pointers:** [Finite-covariance translation bound](../science/05-gaussian-inputs.md#a-finite-covariance-translation-channel-bound); [Gaussian-equivalence boundary](../science/06-related-work.md#why-gaussian-canonical-equivalence-does-not-settle-the-result); [anchor bridge](anchor-and-bridge.md).

### M27 — Compare all Gaussian block input states

- **ID / phase:** M27 · Phase II.
- **Central question:** Do correlations between Gaussian physical inputs restore an unbounded coherent-information rate?
- **Understanding target:** Account for at most one sign qubit per mode, apply the radial variance bound, and use degradability/data processing to extend the energy-independent bound to arbitrary correlated multimode Gaussian input states.
- **Dependencies / story role:** Uses M24–M26; proves that the non-Gaussian lower construction eventually exceeds the entire Gaussian-input coherent-information benchmark.
- **Conceptual connection:** A restriction on physical input-state Gaussianity is not an impossibility theorem for every circuit containing Gaussian components, mixtures or non-Gaussian logical data.
- **Source pointers:** [Applying the Gaussian bound](../science/05-gaussian-inputs.md#applying-the-bound-to-physical-gaussian-states); [meaning of the comparison](../science/07-interpretation.md#what-the-gaussian-input-comparison-means); [anchor bridge](anchor-and-bridge.md).

### M28 — Translate rate into charged physical resources

- **ID / phase:** M28 · Phase II.
- **Central question:** What energy must be increased to transmit more qubits, and which implementation costs remain outside the theorem?
- **Understanding target:** Invert the capacity law into a double-exponential photon requirement, keep finite bounds distinct from exact capacity, and calculate the drive's linear-in-input mean energy injection at fixed noise variance.
- **Dependencies / story role:** Uses M16, M24 and M27; returns the information-theoretic result to its physical resource meaning.
- **Conceptual connection:** Including mean drive-added oscillator energy preserves the leading law but does not price preparation complexity, recovery work, propagation time or error correction in hardware.
- **Source pointers:** [Drive energy accounting](../science/01-model.md#energy-supplied-by-the-fluctuating-drive); [physical interpretation](../science/07-interpretation.md); [finite-bound calculations](../verification/capacity_bounds.py); [anchor bridge](anchor-and-bridge.md).

### M29 — Locate the actual scientific addition

- **ID / phase:** M29 · Phase II.
- **Central question:** Which conclusion remains after the nearest coordinate, subsystem, dephasing and classical fading results are credited?
- **Understanding target:** Separate the inherited random-squeeze/log-coordinate mechanism and QSP qubit from the new matched physical-energy law; compare compact phase noise, Weyl displacements and classical double-logarithmic fading under their actual tasks.
- **Dependencies / story role:** Uses M15, M24 and M28; consolidates attribution and the conditions under which comparisons are meaningful.
- **Conceptual connection:** Neither noise dimension alone nor a familiar change of coordinates determines capacity independently of the generator and charged energy observable.
- **Source pointers:** [Related-work account](../science/06-related-work.md); [primary bibliography](../references/README.md); [relation to other oscillator noise](../science/07-interpretation.md#relation-to-other-oscillator-noise); [anchor bridge](anchor-and-bridge.md).

### M30 — Synthesize the complete capacity story

- **ID / phase:** M30 · Phase II.
- **Central question:** How do the code, environment, converse and Gaussian comparison explain one consistent physical frontier?
- **Understanding target:** Connect log-position energy geometry to growing finite-energy subspaces, fixed environmental resolution, the all-code heat-trace upper bound and bounded Gaussian-input coherent information; retain the fixed-positive-noise limit and the exact model restrictions in the final conclusion.
- **Dependencies / story role:** Final synthesis of M13–M29, using the framework assembled in M12; expresses the full result without replacing scope-qualified rates by hardware or robustness claims.
- **Conceptual connection:** The inherited exact qubit, unbounded double-logarithmic capacity and failure of Gaussian input states to attain that growing rate answer three compatible questions about the same channel.
- **Source pointers:** [Scientific route](../science/README.md); [principal theorem and model](../science/01-model.md); [achievability](../science/02-achievability.md); [converse](../science/03-converse.md); [Gaussian inputs](../science/05-gaussian-inputs.md); [interpretation](../science/07-interpretation.md); [anchor bridge](anchor-and-bridge.md).
