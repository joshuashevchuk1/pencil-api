
default_json = {
            "init_pars": {
                "cvsid": "'$Id$'",
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
                "lnrho_const":0.,
                "ldensity_nolog":True,
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
            "pointmasses_init_pars":{
                "initxxq":"'fixed-cm'",
                "initvvq":"'fixed-cm'",
                "GNewton":1.0,
                "pmass":[1e-4,1.],
                "xq0":[-1,0],
                "lcylindrical_gravity_nbody":[True,True],
                "iprimary":2,
                "ipotential_pointmass":["'boley'","'newton'"],
                "frac_smooth":0.03
            },
        }

class PencilInitResolver:
    def __init__(self):
        self.init_json = None
        self.file_name = None
        return

    def set_init_json(self, init_json):
        self.init_json = init_json

    def set_file_name(self,file_name):
        self.file_name = file_name

    @staticmethod
    def __build_section__(name, params):
        section = f"&{name}\n"
        for key, value in params.items():
            if isinstance(value, list):
                value = ", ".join(map(str, value))
            elif isinstance(value, bool):
                value = "T" if value else "F"
            section += f"  {key} = {value}\n"
        section += "/\n"
        return section

    def __build_file__(self):
        if self.init_json is None:
            self.init_json = default_json
        content = "!  -*-f90-*-  (for Emacs)    vim:set filetype=fortran:  (for vim)\n!\n"
        for section, params in self.init_json.items():
            content += self.__build_section__(section, params) + "\n"
        return content

    def write_file(self):
        configurable_file = self.__build_file__()
        with open("../../../" + str(self.file_name), "w") as file:
            file.write(configurable_file)