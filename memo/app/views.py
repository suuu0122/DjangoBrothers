from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import MemoForm
from .models import Memo



def index(request):
    memos = Memo.objects.all().order_by("-updated_datetime")
    return render(request, "app/index.html", {"memos": memos})



def detail(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    return render(request, "app/detail.html", {"memo": memo})



def new_memo(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app:index")
    else:
        form = MemoForm
    return render(request, "app/new_memo.html", {"form": form})



@require_POST
def delete_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect("app:index")