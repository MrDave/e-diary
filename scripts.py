from datacenter.models import Schoolkid, Mark


def fix_marks(schoolkid: Schoolkid):
    kid_marks = Mark.objects.filter(schoolkid=schoolkid)
    kid_bad_marks = kid_marks.filter(points__lte=3)
    kid_bad_marks.update(points=5)
