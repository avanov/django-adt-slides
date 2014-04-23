def a_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            process_data(form)
            return HttpResponseRedirect('/success/')
    else:
        form = ExampleForm()

    return render(request, 'example.html', {'form': form})
