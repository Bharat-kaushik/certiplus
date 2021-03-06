from django.shortcuts import render

from inet.models import SectionCategory
from inet.models import GrowSection,News,WelcomeLine
from userPlus.models import Logo


def fetch_category_items(request):
    categories = SectionCategory.objects.all()
    logo = Logo.objects.all().first()
    news = News.objects.all()
    welcome = WelcomeLine.objects.all().first()
    print(welcome.first_name)
    # print((categories))

    all_sections = dict()
    for category in categories:
        section = GrowSection.objects.filter(section_category=category)

        if len(section) >= 1:
            title = category.title
            all_sections[title] = section

        else:
            continue

    icon ={"logo": logo}

    return render(request, 'home2.html', {"context": all_sections, "logo": icon,"news":news,"welcome":welcome})