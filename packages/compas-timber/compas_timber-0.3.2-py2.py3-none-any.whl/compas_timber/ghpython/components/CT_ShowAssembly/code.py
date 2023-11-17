from compas.artists import Artist
from ghpythonlib.componentbase import executingcomponent as component
from Grasshopper.Kernel.GH_RuntimeMessageLevel import Warning


class ShowAssembly(component):
    def RunScript(self, Assembly):
        if not Assembly:
            self.AddRuntimeMessage(Warning, "Input parameter Assembly failed to collect data")
            return

        Brep = []
        for beam in Assembly.beams:
            Brep.append(Artist(beam.geometry, context="Grasshopper").draw())

        return Brep
