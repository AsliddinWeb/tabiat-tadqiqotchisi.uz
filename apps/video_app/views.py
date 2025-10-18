from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Video, ContactMessage
import requests
from django.conf import settings


def home_page(request):
    return render(request, 'home.html')


def about_page(request):
    return render(request, 'about.html')


def videos_page(request):
    videos = Video.objects.all().order_by('video_number')
    ctx = {
        'videos': videos
    }
    return render(request, 'videos.html', ctx)


def send_telegram_message(full_name, phone, message):
    """Telegram botga xabar yuborish"""
    try:
        bot_token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID

        text = f"""
🆕 Yangi xabar!

👤 Ism: {full_name}
📱 Telefon: {phone}
💬 Xabar:
{message}
        """

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML"
        }

        response = requests.post(url, data=data)
        return response.status_code == 200
    except Exception as e:
        print(f"Telegram xabar yuborishda xatolik: {e}")
        return False


def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        message_text = request.POST.get('message', '').strip()

        # Validatsiya
        if not full_name or not phone or not message_text:
            messages.error(request, "Iltimos, barcha maydonlarni to'ldiring!")
            return redirect('contact_page')

        # Ma'lumotlarni saqlash
        contact_message = ContactMessage.objects.create(
            full_name=full_name,
            phone=phone,
            message=message_text
        )

        # Telegramga yuborish
        if send_telegram_message(full_name, phone, message_text):
            contact_message.is_sent_to_telegram = True
            contact_message.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz.")
        else:
            messages.warning(request, "Xabaringiz saqlandi, lekin telegramga yuborishda muammo yuz berdi.")

        return redirect('contact_page')

    return render(request, 'contact.html')
