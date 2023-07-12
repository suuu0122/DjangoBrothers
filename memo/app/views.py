from django.shortcuts import get_object_or_404, render

from .models import Memo



def index(request):
    memos = Memo.objects.all().order_by("-updated_datetime")
    return render(request, "app/index.html", {"memos": memos})



def detail(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    return render(request, "app/detail.html", {"memo": memo})



def new_memo(request):
    return render(request, "app/new_memo.html")