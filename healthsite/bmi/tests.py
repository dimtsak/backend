def home(request):
    errors = {}
    context = {}
    if request.method=="POST":
        weight_metric = request.POST.get("weight-metric")
        weight_imperial = request.POST.get("weight-imperial")

        if weight_metric:
            try:
                weight = float(request.POST.get("weight-metric"))
            except ValueError :
                errors['invalid'] = 'Invalid weight input!'
                return render(request,'bmi/index.html',errors)

            height = request.POST.get("height-metric")

            if ',' in height.split():
                errors['invalid'] = 'Not , in height!Give decimal points with a . '
                return render(request,'bmi/index.html',errors)

            try:
                height = float(request.POST.get("height-metric"))
            except ValueError :
                errors['invalid'] = 'Invalid input!Height must be a number the decimal points of which should be seperated with a dot .'
                return render(request,'bmi/index.html',errors)


        elif weight_imperial:
            try:
                weight = float(request.POST.get("weight-imperial"))/2.205
            except ValueError :
                errors['invalid'] = 'Invalid input for imperial weight! '
                return render(request,'bmi/index.html',errors)
            try:
                height = (float(request.POST.get("feet"))30.48 + float(request.POST.get("inches"))2.54)/100
            except ValueError :
                errors['invalid'] = 'Invalid input!Give valid values for height  imperial!'
                return render(request,'bmi/index.html',errors)

        bmi = (weight/(height**2))
        save = request.POST.get("save")
        if save == "on":
            Bmi.objects.create(user=request.user,weight=weight, height=height, bmi=round(bmi))
        if bmi < 16:
            state = "Thin(Severe)"
        elif bmi > 16 and bmi < 17:
            state = "Thin(Mild)"
        elif bmi > 17 and bmi < 18:
            state = "Thin"
        elif bmi > 18 and bmi < 25:
            state = "Normal"
        elif bmi > 25 and bmi < 30:
            state = "Overweight"
        elif bmi > 30 and bmi < 35:
            state = "Obese Class I"
        elif bmi > 35 and bmi < 40:
            state = "Obese Class II"
        elif bmi > 40:
            state = "Obese Class III"

        context["bmi"] = round(bmi)
        context["state"] = state

    return render(request, "bmi/index.html", context)  
    

    '''def raiseValueError(val,message):
    errors = {}
    try:
        val = float(val)
    except ValueError:
        errors['Value'] = message
        return message
    return None '''