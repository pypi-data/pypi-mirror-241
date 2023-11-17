# autodevice

Automatically assign devices in-line with pytorch code

### Usage

```python
from autodevice import AutoDevice

x = torch.randn([200, 50]).to(AutoDevice())
```
CUDA/GPU:
```
tensor([[ 2.6905, -0.3037, -0.3607],
        [ 0.2258, -0.1755,  0.6599],
        [ 1.3046, -0.9389,  0.7358]], device='cuda:0')
```
CPU:
```
tensor([[ 2.6905, -0.3037, -0.3607],
        [ 0.2258, -0.1755,  0.6599],
        [ 1.3046, -0.9389,  0.7358]])
```
On Apple Silicon (M1, M2):
```
tensor([[ 0.5382,  1.1173,  1.1175],
        [-0.0125, -0.2406,  0.2343],
        [-0.6067, -0.7728,  0.1697]], device='mps:0')
```
### Installation

```
pip install autodevice
```
