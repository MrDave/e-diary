from datacenter.models import Schoolkid, Mark, Chastisement


def fix_marks(schoolkid: Schoolkid):
    kid_marks = Mark.objects.filter(schoolkid=schoolkid)
    kid_bad_marks = kid_marks.filter(points__lte=3)
    kid_bad_marks.update(points=5)


def remove_chastisements(schoolkid: Schoolkid):
    kid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    kid_chastisements.delete()
