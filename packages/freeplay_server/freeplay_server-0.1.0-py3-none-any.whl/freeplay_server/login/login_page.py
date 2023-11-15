import logging

import stytch
from flask import Blueprint, render_template, request, url_for, redirect, session
from flask.typing import ResponseReturnValue

from freeplay_server.accounts.accounts_repository import AccountsRepository
from freeplay_server.accounts.users import Roles
from freeplay_server.auth.auth_filter import public_endpoint, allow_role

logger = logging.getLogger(__name__)

# Email magic link sessions expire after 7 days, specified in minutes.
SEVEN_DAYS_IN_MINUTES = 10080


def login_page(
        stytch_client: stytch.Client,
        base_url: str,
        stytch_public_token: str,
        accounts_repo: AccountsRepository
) -> Blueprint:
    page = Blueprint('login_page', __name__, url_prefix='/login')

    @public_endpoint
    @page.get('')
    def show() -> ResponseReturnValue:
        return render_template(
            'login.html',
            authenticate_url=f'{base_url}{url_for("login_page.authenticate")}',
            stytch_public_token=stytch_public_token
        )

    # This is the endpoint the link in the magic link hits.
    # It takes the token from the link's query params and hits the
    # stytch authenticate endpoint to verify the token is valid
    @public_endpoint
    @page.get("/authenticate")
    def authenticate() -> ResponseReturnValue:
        resp = stytch_client.magic_links.authenticate(
            request.args.get("token"),
            session_duration_minutes=SEVEN_DAYS_IN_MINUTES
        )

        if resp.status_code != 200:
            logger.error('Received an error from stytch while trying to authenticate user %s', resp.user_id)
            logger.error(f'Response from Stytch: "{resp}"')
            return "Unable to authenticate user. Please contact your account administrator or support@freeplay.ai for help."

        user = accounts_repo.find_user_by_stytch_user_id(resp.user_id)
        if user is None:
            logger.error('Unable to find user %s', resp.user_id)
            return "Unable to authenticate user. Please contact your account administrator or support@freeplay.ai for help."

        session['user_id'] = user.id

        return redirect('/projects')

    @allow_role(Roles.ACCOUNT_USER)
    @page.get("/logout")
    def logout() -> ResponseReturnValue:
        session.clear()
        return redirect('/login')

    return page
