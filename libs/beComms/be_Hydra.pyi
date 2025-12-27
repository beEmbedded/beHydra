##########################################################
################### PUBLIC API'S #########################
##########################################################

class BEHYDRA:
    beHydraConfig dict
    
    @classmethod
    def get_fw_version(cls): ...
    
    @classmethod
    def get_license(cls): ...
    
    @classmethod
    def get_hw_version(cls): ...
    
    @classmethod
    def scan_comPort(cls): ...
    
    @classmethod
    def get_detected_module(cls): ...
    
    @classmethod
    def set_comPort(cls, com_port: str) -> bool: ...      
    
    @classmethod
    def get_comPort(cls): ...
    
    @classmethod
    def reset(cls): ...

    @classmethod
    def get_router_input(cls, inputId): ...
    
    @classmethod
    def get_router_output(cls, inputId, outputId): ...
    
    @classmethod
    def get_router_all(cls): ...