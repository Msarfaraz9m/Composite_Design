def get_modulus_of_elasticity_upper_bound(inp1, inp2, inp3, inp4):
    elastic_modulus_matrix = float(inp1)
    volume_fraction_matrix = float(inp2)
    elastic_modulus_particulate = float(inp3)
    volume_fraction_particulate = float(inp4)
    moeUB = (elastic_modulus_matrix*volume_fraction_matrix)+(elastic_modulus_particulate*volume_fraction_particulate)
    return moeUB


def get_modulus_of_elasticity_lower_bound(inp1, inp2, inp3, inp4):
    elastic_modulus_matrix = float(inp1)
    volume_fraction_matrix = float(inp2)
    elastic_modulus_particulate = float(inp3)
    volume_fraction_particulate = float(inp4)
    moeLB = ((elastic_modulus_matrix*elastic_modulus_particulate)/((volume_fraction_matrix*elastic_modulus_particulate)+(volume_fraction_particulate*elastic_modulus_matrix)))
    return moeLB


def get_critical_fiber_length(inp1, inp2, inp3):
    ultimate_tensile_strength = float(inp1)
    fiber_diameter = float(inp2)
    shear_yield_strength = float(inp3)
    cfl = ((ultimate_tensile_strength * fiber_diameter) / (2 * shear_yield_strength))
    return cfl


def get_is_continuous(inp8, critical_fiber_length):
    fiber_length = float(inp8)
    if fiber_length > 15 * critical_fiber_length:
        return True
    else:
        return False


def get_longitudinal_stress(inp1, inp2, inp3, inp4,inp5):
    stress_matrix_phase = float(inp1)
    stress_fiber_phase = float(inp2)
    area_matrix_phase = float(inp3)
    area_fiber_phase = float(inp4)
    area_composite = float(inp5)
    ls = ((stress_matrix_phase * area_matrix_phase / area_composite) + (
                stress_fiber_phase * area_fiber_phase / area_composite))
    return ls


def get_elasticity_longitudinal(inp1, inp2, inp3, inp4):
    elasticity_matrix = float(inp1)
    volume_fraction_matrix = float(inp2)
    elasticity_fiber = float(inp3)
    volume_fiber = float(inp4)
    el = ((elasticity_matrix * volume_fraction_matrix) + (elasticity_fiber * volume_fiber))
    return el


def get_elasticity_transverse(inp1, inp2, inp3, inp4):
    elasticity_matrix = float(inp1)
    volume_fraction_matrix = float(inp2)
    elasticity_fiber = float(inp3)
    volume_fiber = float(inp4)
    #volume_fraction_particulate = float(inp5)
    et = ((elasticity_matrix * elasticity_fiber) / (
                (volume_fraction_matrix * elasticity_fiber) + (volume_fiber * elasticity_matrix)))
    return et
