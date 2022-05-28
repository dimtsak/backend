def addproduct(request):
    errors = {}
    product_set = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        name = request.POST.get('name')
        commercial_name = request.POST.get('commercial_name')
        for product in product_set.iterator():
            if product.commercial_name == commercial_name:
                errors["Existing"] = 'This commercial name already exists!'
                errors['form'] = form
                return render(request,'store/create.html',errors)

        digits_in_name = checkForDigits(name)
        digits_in_com_name = checkForDigits(commercial_name)
        if digits_in_name:
            errors['Digits'] = digits_in_name
            errors['form'] = form
            return render(request,'store/create.html',errors)
        if digits_in_com_name:
            errors['Digits'] = digits_in_com_name
            return render(request,'store/create.html',errors)



        if form.is_valid():
            form.save()
            return redirect('adminpanel')
    context ={
        'form':form,
    }
    return render(request,'store/create.html',context)



