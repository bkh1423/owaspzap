from django.shortcuts import render

def scan_test(request):
    target = None

    if request.method == "POST":
        target = request.POST.get("target")

    return render(request, "scans/scan_test.html", {
        "target": target
    })
