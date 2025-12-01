from django.contrib.auth.models import Group


def is_company_user(user):
    """Return True if the given Django user should be considered a 'Company'.

    This is resilient to several common project setups:
    - custom boolean flag `is_company`
    - a related `company` attribute (profile or FK)
    - a `company_name` attribute
    - membership in a `Company` group
    """
    if user is None or not getattr(user, 'is_authenticated', False):
        return False

    if getattr(user, 'is_company', False):
        return True

    if hasattr(user, 'company') and getattr(user, 'company'):
        return True

    if hasattr(user, 'company_name') and getattr(user, 'company_name'):
        return True

    try:
        return user.groups.filter(name__iexact='company').exists()
    except Exception:
        return False


def is_owner_of_job(job, user):
    """Return True if `user` is the owner/creator of `job`.

    Handles common patterns: job has `posted_by`, `owner`, or `company_name` fields.
    """
    if user is None or job is None:
        return False

    # Direct owner attribute
    if hasattr(job, 'owner') and getattr(job, 'owner') is not None:
        if job.owner == user:
            return True

    # Common case: job.posted_by might be a Company profile or the User
    if hasattr(job, 'posted_by') and getattr(job, 'posted_by') is not None:
        posted = job.posted_by
        # posted_by might refer to the company profile linked on the User
        if posted == user:
            return True
        # compare to user's company relation if present
        user_company = getattr(user, 'company', None)
        if user_company is not None and posted == user_company:
            return True
        # compare simple company_name fields if present
        posted_name = getattr(posted, 'company_name', None) or getattr(posted, 'name', None)
        user_name = getattr(user, 'company_name', None) or getattr(user, 'company_name', None)
        if posted_name and user_name and posted_name == user_name:
            return True

    # fallback: compare by company_name on job directly
    if hasattr(job, 'company_name'):
        if getattr(job, 'company_name') and getattr(user, 'company_name') and job.company_name == user.company_name:
            return True

    return False
