from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from CalculateDesign.Calculations import *


def index(request):
    return render(request, 'index.html')


def validate_modulus_of_elasticity(inp1, inp2, inp3, inp4):
    if(len(inp1) == 0 or len(inp2) == 0 or len(inp3) == 0 or len(inp4) == 0
            or inp1 == 0 or inp2 == 0 or inp3 == 0 or inp4 == 0):
        return False
    return True


def validate_longitudinal_stress(inp1, inp2, inp3, inp4, inp5):
    if(len(inp1) == 0 or len(inp2) == 0 or len(inp3) == 0 or len(inp4) == 0 or len(inp5) == 0
            or inp1 == 0 or inp2 == 0 or inp3 == 0 or inp4 == 0 or inp5 == 0):
        return False
    return True


def modulus_of_elasticity(request):
    if request.method == 'POST':
        dt = request.POST
        inp1 = dt.get('inp1')
        inp2 = dt.get('inp2')
        inp3 = dt.get('inp3')
        inp4 = dt.get('inp4')
        if(validate_modulus_of_elasticity(inp1, inp2, inp3, inp4)):
            ub = get_modulus_of_elasticity_upper_bound(inp1, inp2, inp3, inp4)
            lb = get_modulus_of_elasticity_lower_bound(inp1, inp2, inp3, inp4)
            result = {
                "lb": lb, "ub": ub, "inp1": inp1, "inp2": inp2, "inp3": inp3, "inp4": inp4
            }
            return render(request, 'modulus_of_elasticity.html', result)
        else:
            return render(request, 'modulus_of_elasticity.html')
    else:
        return render(request, 'modulus_of_elasticity.html')


def critical_fiber_length(request):
    if request.method == 'POST':
        dt = request.POST
        inp1 = dt.get('inp1')
        inp2 = dt.get('inp2')
        inp3 = dt.get('inp3')
        inp4 = dt.get('inp4')
        if(validate_modulus_of_elasticity(inp1, inp2, inp3, inp4)):
            cfl = get_critical_fiber_length(inp1, inp2, inp3)
            if(get_is_continuous(inp4, cfl)):
                ic = "continuous"
            else:
                ic = "discontinuous/short"
            result = {
                "cfl": cfl, "ic": ic, "inp1": inp1, "inp2": inp2, "inp3": inp3
            }
            return render(request, 'critical_fiber_length.html', result)
        else:
            return render(request, 'critical_fiber_length.html')
    else:
        return render(request, 'critical_fiber_length.html')


def stress(request):
    if request.method == 'POST':
        dt = request.POST
        inp1 = dt.get('inp1')
        inp2 = dt.get('inp2')
        inp3 = dt.get('inp3')
        inp4 = dt.get('inp4')
        inp5 = dt.get('inp5')
        if(validate_longitudinal_stress(inp1, inp2, inp3, inp4, inp5)):
            ls = get_longitudinal_stress(inp1, inp2, inp3, inp4, inp5)            
            result = {
                "ls": ls, "inp1": inp1, "inp2": inp2, "inp3": inp3, "inp4": inp4, "inp5": inp5
            }
            return render(request, 'stress.html', result)
        else:
            return render(request, 'stress.html')
    else:
        return render(request, 'stress.html')


def elasticity(request):
    if request.method == 'POST':
        dt = request.POST
        inp1 = dt.get('inp1')
        inp2 = dt.get('inp2')
        inp3 = dt.get('inp3')
        inp4 = dt.get('inp4')
        if(validate_modulus_of_elasticity(inp1, inp2, inp3, inp4)):
            td = get_elasticity_transverse(inp1, inp2, inp3, inp4)
            ld = get_elasticity_longitudinal(inp1, inp2, inp3, inp4)
            result = {
                "td": td, "ld": ld, "inp1": inp1, "inp2": inp2, "inp3": inp3, "inp4": inp4
            }
            return render(request, 'elasticity.html', result)
        else:
            return render(request, 'elasticity.html')
    else:
        return render(request, 'elasticity.html')
