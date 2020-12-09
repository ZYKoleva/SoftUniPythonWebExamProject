def validate_creator(ad, user):
    if ad.created_by != user and not user.is_superuser:
        raise PermissionError('Нямате права да променяте и/или изтривате обяви, които не са създадени от вас!')

