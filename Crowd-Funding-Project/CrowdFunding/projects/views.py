from django.shortcuts import render,redirect

# Create your views here.
from .models import Projects
from images.models import Images

from donations.views import all_donated
from django.db.models import Sum


# Create your views here.


def all_projects(request):
    try:
        all_projects = Projects.objects.all()
        for project in all_projects:
            print(project)
            total_donation = project.total_donation
            print("total_donation")
            print(total_donation)
            all_donations = all_donated(request, project.id)
            sumOfDonations = all_donations["donation_amount__sum"]
            Percentage = sumOfDonations / total_donation * 100
            project.donated = sumOfDonations
            project.Percentage = Percentage
            print('donated')
            print(project.donated)
            print('Percentage')
            print(project.Percentage)
            image = Images.objects.filter(project_id=project.id)
            user_id = request.session['user_id']
            for i in image:
                project.main_img_src = (i.img)
            context = {
                'all_projects': all_projects,
                "user_id": user_id
            }
        return render(request, 'projects.html', context)
    except:
        return redirect("/login/")


def get_img(id):
    image = Images.objects.filter(project_id=id)
    for i in image:
        print(i)
    render(i)


def project_details(request, id):
    try:
        project_details = Projects.objects.get(id=id)
        all_donations = all_donated(request, id)
        total_donation = project_details.total_donation
        print(total_donation)
        sumOfDonations = all_donations["donation_amount__sum"]
        print(sumOfDonations)
        Percentage = sumOfDonations / total_donation * 100
        print(Percentage)
        images_list = []
        image = Images.objects.filter(project_id=id)
        user_id = request.session['user_id']
        for i in image:
            images_list.append(i.img)
        print(images_list)

        context = {
            'project': project_details,
            'sumOfDonations': sumOfDonations,
            'Percentage': Percentage,
            'images_list': images_list,
            "user_id": user_id
        }
        return render(request, 'project_details.html', context)
    except:
        return redirect("/login/")


def add_project(request):
    try:
        user_id = request.session['user_id']
        context = {
            "user_id": user_id
        }
        return render(request, 'addprojects.html', context)
    except:
        return redirect("/login/")
