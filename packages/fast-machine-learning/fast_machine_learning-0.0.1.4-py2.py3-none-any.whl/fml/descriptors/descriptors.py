
import joblib, glob, pathlib, numpy as np
selfpath = pathlib.Path(__file__).parent.resolve()
if __name__ == "__main__":
    from utils import JobLibFileClass
else:
    from .utils import JobLibFileClass

class AtomDescriptors:
    
    def __init__(self):
        joblibs = glob.glob(str(pathlib.Path(selfpath, "*.joblib")))
        self.joblibnames = []
        for joblib_ in joblibs:
            joblibname = pathlib.Path(joblib_.split(".")[0]).parts[-1]
            data = joblib.load(joblib_)
            self.joblibnames.append(joblibname)
            self.__dict__[joblibname] = data
    def __call__(self, atom=None, descriptor_name=None):
        pass



if __name__ == "__main__":
    des = AtomDescriptors()
    
    v = des.v
    m = des.m
    m_meaning = des.m_meaning
    m_ionradii = des.m_ionic_radii
    m_ionenergy = des.m_ionic_energies
    m_oxi = des.m_ionic_oxidation_states
    og = des.organic_descriptors
    ol = des.organic_list
    b3 = des.c9tc06632b3
    b4 = des.c9tc06632b4