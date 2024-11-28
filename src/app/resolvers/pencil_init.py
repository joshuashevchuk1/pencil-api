
default_config = {
            "init_pars": {
                "cvsid": "$Id$",
                "ip": 6,
                "xyz0": [-2.6, -2.6, -0.26],
                "xyz1": [2.6, 2.6, 0.26],
                "lperi": [True, True, True],
                "r_int": 0.4,
                "r_ext": 2.5,
                "lcylinder_in_a_box": True,
                "llocal_iso": True,
                "lcylindrical_gravity": True
            },
            "initial_condition_pars": {
                "temperature_power_law": 1,
                "density_power_law": 0
            },
            "eos_init_pars": {
                "cs0": 0.05,
                "rho0": 1.0,
                "gamma": 1.0
            },
            "hydro_init_pars":{},
            "density_init_pars":{
                "lnrho_const":0,
                "ldensity_nolong":True,
            },
            "grav_init_pars":{
                "ipotential":"no-smooth",
                "g0": 1
            },
            "special_init_pars":{},
            "particles_init_pars":{
                "initxxp":"random",
                "initvvp":"random",
                "eps_dtog":0.01
            },
            "pointmasses_init_pars":{},
                "initxxq":'fixed-cm',
                "initvvq":'fixed-cm',
                "GNewton":1.0,
                "pmass":[1e-4,1.],
                "xq0":-1.0,
                "lcylindrical_gravity_nbody":[True,True],
                "iprimary":2,
                "ipotential_pointmass":['boley','newton'],
                "frac_smooth":0.03
        }

class PencilInitResolver:
    def __init__(self):
        return

    def build_section(self,name, params):
        section = f"&{name}\n"
        for key, value in params.items():
            if isinstance(value, list):
                value = ", ".join(map(str, value))
            elif isinstance(value, bool):
                value = "T" if value else "F"
            section += f"  {key} = {value}\n"
        section += "/\n"
        return section

    def build_file(self, config=None):
        if config is None:
            config = default_config
        content = "!  -*-f90-*-  (for Emacs)    vim:set filetype=fortran:  (for vim)\n!\n"
        for section, params in config.items():
            content += self.build_section(section, params) + "\n"
        return content

    def save_file(self):
        configurable_file = self.build_file()
        with open("../../../start.in", "w") as file:
            file.write(configurable_file)