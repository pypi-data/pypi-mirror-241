from datetime import timedelta

from ibes.sim.simulation import create_sim
from ibes.objects.pools import MassPool
from ibes.objects.organisms import Daphnia, Organism
from ibes.objects.environments import World
from ibes.sim.experiment import Experiment, Observation
from ibes.objects.housekeeping import Event, BALANCE, CLOCK, SCHEDULE, LOGGER

def test_minimal_setup():
    w = World()
    o = Organism(X0={"Body":{"mass":1}}, environment=w)
    CLOCK.dt = timedelta(1)
    o.step()

def test_minimal_sim():
    s = create_sim()
    LOGGER.reset()
    LOGGER.default(level="ERROR")
    s.run()
    s.assert_mass_conservation_final()
    s.end()

def test_manual_sim():
    """
    test whether there are errors in the mass balance fluxes. This means 
    the sum of all sums of fluxes should be zero (or due to rounding errors
    very close to zero)
    """
    # assert False
    # set up the simulation (always has to go first!)
    CLOCK.reset()
    BALANCE.reset()
    SCHEDULE.reset()
    LOGGER.reset()
    LOGGER.default(level="ERROR")
    CLOCK.dt_target = timedelta(seconds=3600)
    CLOCK.time = timedelta(0)
    CLOCK.stop = timedelta(hours=7*24)
    CLOCK.adapt_dt(SCHEDULE)
    BALANCE.dimension = MassPool

    # initialize simulated objects
    w = World(
        X0={"Food": {"mass": 0}},
        structure_params={"Water": {"volume": 80}},
    )
    d = Daphnia(
        environment=w,
        X0={"Body": {"mass": 0.2}, "Repair": {"rate": 0.00001}},
        structure_params={"Body": {"density": 0.2}},
        distribution=0.5,
        search_rate_max=7.168e-4,
        assimilation_rate_max=3.858e-5,
        maintenance_rate_max=7.947e-8,
        mass_puberty_threshold=0.3,
        spawning_interval=172800,
        egg_dry_mass=2.021e-2,
        birth_success=0.9,
        rate_damage_baseline=0.000000000001,
        rate_repair_decay=0.0000000000008
    )

    
    # set up the experiment (i.e. external events)
    e = Experiment(environment=w, observation_type=Observation)
    feedevent = Event(
        time=timedelta(hours=1), 
        instance=e, 
        method=e.feed_mg_carbon,
        arguments=(1,)
    )
    SCHEDULE.add(feedevent)

    while CLOCK.time <= CLOCK.stop:
        # execute events scheduled during step consumes very little time
        SCHEDULE.execute(CLOCK.time)
        BALANCE.sum_flux()
        BALANCE.update_pools()

        # continuous step
        if CLOCK.dt > timedelta(0):
            for agent in w.agents:
                agent.step()
                agent.internal_events()

            w.step()
            w.internal_events()

            # inefficient factor 4
            BALANCE.sum_flux()
            BALANCE.update_pools()

        # advance clock
        CLOCK.adapt_dt(SCHEDULE)
        CLOCK.tick()

    assert BALANCE.fluxes_to_df(MassPool)["∑"].sum() <= 1e-15