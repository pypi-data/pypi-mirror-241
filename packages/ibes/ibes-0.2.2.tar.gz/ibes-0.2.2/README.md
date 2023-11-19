# Individual-based experiment simulation

![tests](https://github.com/flo-schu/ibes/actions/workflows/python-package.yml/badge.svg)
![pypi](https://github.com/flo-schu/ibes/actions/workflows/python-publish.yml/badge.svg)

## Introduction

Ibes is a framework for modeling the life cycle of biological organisms as  individuals and populations. The model is designed to ensure consitency of basic thermodynamic principles; most fundamentally the conservation of mass and energy. Ibes addresses modelers who want increased flexibility in their biological systems model design while staying inside a reliable modeling framework. Ibes is not fast compared to methods based solely on differential equations or closed form solutions.

The package was originally designed to write a Python implementation of Dynamic Energy Budgets (DEB) - specifically DEBkiss (Jager, 2018). These models are designed to simulate the life cylce of the model laboratory organism Daphnia Magna. The goal was to analyze effects of exposure to toxicants under adverse environmental conditions of such organisms from laboratory experiments. It quickly became clear that typical lab experiments like OECD Test No. 211 _Daphnia magna Reproduction Test_ imposes adverse conditions on the test organism by the experimental design. Examples of such design flaws are:

- population pressure from offspring between exchange of experimental media,
- non-constant food conditions

To better utilize available data from animal testing, the goal was to incorporate exact laboratory conditions and experimental routines into the DEB model. This cannot be done with conventional approaches and thus the idea of ibes was born.

## Model description

Ibes models can be constructed from very low-level commands up to higher order functions that set up preconfigured experiments that can easily be modified with configuration files.

the simplest possible model

```python
from ibes.objects.organisms import Organism
from ibes.objects.environments import World
w = World()
o = Organism(X0={"Body":{"mass":1}}, environment=w)
CLOCK.dt = timedelta(1)
o.step()
w.step()
```

as can be seen the model acts via step functions that carry out basic routines. `Organism.step()` implements basic functions of life.

Ibes implements organisms as classes. Classes are lending themselves naturally to describe members of the phylogenetic tree of evolution. If one fundamental class has been written, the next description of a Genus, Order, Family, Species can always be built upon its ancestor. This in fact makes the definition of the Daphnia class, a thing of only a few lines of code.

```python
class Daphnia(Invertebrata):
    _ids = count(0)

    def __init__(
        self, 
        rate_uptake_esfenvalerate=0, 
        rate_elimination_esfenvalerate=0,
        **kwargs
        ):  
        super().__init__(**kwargs)

    def spawn_trigger(self):
        """
        For Daphnia reproduction takes place roughly every two days. This may
        be different in other species.
        """
        spawning_time = self.pools[ReproClock].time > self.spawning_interval
        return spawning_time and self.is_adult()
```

Also each organism needs an abiotic World to live in. This is implemented in the `World` class. Depending on what the goal of your model is, `World.step()` can contain different methods, implementing these.

### How are state variables tracked?

Ibes creates mass-pools with the `Pool` class. All these pools are state variables which are tracked and each `MassPool` is automatically contributing to the total mass balance of the system, which needs to stay constant

### How are experiments described?

Experiments can be described with a spreadsheet and a set of methods corresponding to the column names of the spreadsheet. For example the experiment procedure "feeding" can be described as follows:

```python
from ibes.sims.experiment import Experiment
from ibes.objects.base import external_environmental_event

class MyExperiment(Experiment)
    @external_environmental_event
    def feeding_mg(self, param):
        if param == 0:
            pass
        elif param > 0:
            self.flux(param, pool_in=self.env.pools[Food], pool_out=IO)
```

then the only thing needed is an experiment spread sheed listing the times and parameters for `feeding_mg`.

| time   | feeding_mg |
|--------|------------|
| 0 days |    1.0     |
| 1 days |    0.0     |
| 2 days |    2.0     |
| 4 days |    1.0     |
|--------|------------|

Internally at the beginning of the simulation this table is fed to the class `MyExperiment` and all feeding events are scheduled based on their time. When the runtime of the simulation has advanced to the event, it is executed. In the meantime, the organism or population does what it does. Feeding, Reproducing, Dying, ...

time can also be tracked as dates at arbitrary precision (e.g. `05.07.2022 13:42:05`). So, if observations in the experiment were done at different times on different dates and there is a doubt that it might have affected the results, this could also be modelled explicitely. Time in general in this framework is tracked in seconds and multiples

### This seems all very complicated

That is correct, because it is. Luckily, there is a very uncomplicated top-level function that does all the overhead work. The only thing you have to do is changing parameters of the configuration file and of course write your own functions and Organism classes, in case you want to.

```python
CFG1 = read_config("config/parameters/tests/daphnia.json")  # load config file
sim = basic_simulation(CFG1, logging_level_override="ERROR")  # init and run
sim.plot_life_history(store=False, show=True)  # plot the trajectories
```

templates of various config file can be found under <config/parameters/tests/>

## Current state

### Biological systems and functions are built in and can be modelled

- Organisms:
  - Daphnia Magna
- Functions:
  - Survival
  - Growth
  - Reproduction
  - Feeding (functional response)
  - Toxicant uptake and elimination
  - Adverse Outcome Pathways (AOP). Very experimental so far
- Experiments:
  - OECD Test No. 211: Daphnia Magna Reproduction test
  - Population Development of Daphnia Magna

### What ibes cannot do, yet

- simulate movement. This was up until now not necessary, but an implementation
  should be easily possible
- check units and ensure dimensionality consistency. A cause of frustration is
  oftentimes that errors result from conversion to milli, micro, etc.
  An experimental branch exists to utilize sympy for assertion of dimensional model consistency and conversion of units into SI system by default. However, this was not developed so far, but would be very desirable.
- Use symbolic math like sympy or other frameworks using equation graphs, for  
  sped up computation. This feature seemed very inspiring, but we realized that a lot of model freedom would have to be sacrificed to obtain not too impressive speedups.


### General Notes

- Order of columns in events table determines execution order.
- Input of an event file always overrides the `time` configuration in `simulation` in the config.json file


## Installation  

```bash
pip install ibes
```

### Development 


VScode as a texteditor is recommended but not necessary scripts can be run from the commandline, line-by-line or in a debugging environment

Create conda environment
```bash
conda create -n ibes
conda activate ibes
conda install python=3.11
```

For installing a development version and actively and iteratively update and develop it it is recommended to download from source and install as editable
Clone respository, change into directory and install.
```bash
git clone git@github.com:flo-schu/ibes.git
cd ibes
pip install --editable .[dev]
```

It is recommended to run tests and see if everything works as expected in your
shell type `pytest` see <https://docs.pytest.org/en/7.1.x/> for more info
```bash
pytest
```
