# -*- coding: utf-8 -*-
# import settings

class submissionRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on submission models to 'local_env454'"
        if model._meta.app_label == 'submission':
            return 'local_env454'
        # if model._meta.app_label == 'submission':
        #     return 'local_env454'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on submission models to 'local_env454'"
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('local_env454', 'test_vamps')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

        # "Allow any relation if a both models in submission app"
        # if obj1._meta.app_label == 'submission' and obj2._meta.app_label == 'submission':
        #     return True
        # # Allow if neither is submission app
        # elif 'submission' not in [obj1._meta.app_label, obj2._meta.app_label]: 
        #     return True
        # return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return False


    def allow_syncdb(self, db, model):
        if db == 'test_vamps' or db == 'local_env454' or model._meta.app_label == "submission":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True

# class DatabaseAppsRouter(object):
# http://diegobz.net/2011/02/10/django-database-router-using-settings/
