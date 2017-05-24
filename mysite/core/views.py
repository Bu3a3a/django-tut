import json
import telepot
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.http import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse



TELEGRAM_BOT_TOKEN = '308828925:AAFbww2ge3WxWcsYDXsdy5-PlLBCQWS97QQ'

bot = telepot.Bot(TELEGRAM_BOT_TOKEN)


def _display_help():
    return 'you asked for helpo? ahaha'


#def _display_planetpy_feed():
   # return render_to_string('feed.md', {'items': parse_planetpy_rss()})
def repeat_all_messages(message): # Название функции не играет никакой роли, в $
    bot.sendMessage(message.chat.id, message.text)



class CommandReceiveView(generic.View):
    def post(self, request, bot_token):
        if bot_token != TELEGRAM_BOT_TOKEN:
            return HttpResponseForbidden('Invalid token')

        commands = {
            '/start': _display_help,
            'help': _display_help,
            'feed': repeat_all_messages,
        }

        raw = request.body.decode('utf-8')

        try:
            payload = json.loads(raw)
        except ValueError:
            return HttpResponseBadRequest('Invalid request body')
        else:
            chat_id = payload['message']['chat']['id']
            cmd = payload['message'].get('text')  # command

            func = commands.get(cmd.split()[0].lower())
            if func:
                bot.sendMessage(chat_id, func(), parse_mode='Markdown')
            else:
                bot.sendMessage(chat_id, 'I do not understand you, Sir!')

        return JsonResponse({}, status=200)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CommandReceiveView, self).dispatch(request, *args, **kwargs)



class IndexView(generic.TemplateView):
    template_name = 'core/index.html'


class LoginView(auth_views.LoginView):
    template_name = 'core/login.html'


class LogoutView(auth_views.LogoutView):
    template_name = 'core/logout.html'


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'core/password_reset.html'
    success_url = reverse_lazy('core:password_reset_done')
    email_template_name = 'core/password_reset_email.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('core:password_reset_complete')
    template_name = 'core/password_reset_confirm.html'


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'core/password_reset_complete.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'core/password_reset_done.html'


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    login_url = reverse_lazy('core:login')
    template_name = 'core/profile.html'

    # def get_context_data(self, **kwargs):
    #
    #     return super().get_context_data(**kwargs)
