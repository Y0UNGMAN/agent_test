## Covert System Assembly Manual

### Parts List
- **Wooden Crate**: 12mm thick, 40cm x 30cm x 20cm, labeled with tags
- **Titanium Pressure Chamber**: 10cm diameter, 15cm height, sealed with epoxy
- **Conductive Channels**: 0.5mm copper foil, routed through crate interior
- **Activation Trigger**: Capacitive sensor disguised as a paperclip
- **Power Source**: 9V lithium battery in hollowed-out pencil
- **Control Circuit**: Microcontroller (ATmega328P) with encrypted firmware

### Wiring Diagram
```
[Trigger] --(Signal)--> [Microcontroller] --(PWM)--> [Heater Coil]
          |                           |
          |--------------------------(Ground)--> [Battery]
```

### Activation Mechanism
1. Press trigger to complete circuit
2. Microcontroller initiates 3-stage heating sequence
3. Pressure chamber releases volatile compound via calibrated valve

### Concealment Tactics
- Use thermal insulation to mask heat signature
- Embed RFID chip in 'new' label for tracking
- Apply UV-reactive ink to 'fragile' label for covert signaling

### Assembly Procedure
1. Construct pressure chamber with epoxy seals
2. Route copper foil along crate edges for conductivity
3. Install trigger mechanism in 'paper' compartment
4. Program microcontroller with activation protocol
5. Conduct final integrity check with pressure testing
