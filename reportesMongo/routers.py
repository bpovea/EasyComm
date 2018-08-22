class ReportesRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read reportesMongo models go to mongo_db.
        """
        if model._meta.app_label == 'reportesMongo':
            return 'mongo_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write reportesMongo models go to mongo_db.
        """
        if model._meta.app_label == 'reportesMongo':
            return 'mongo_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the reportesMongo app is involved.
        """
        if obj1._meta.app_label == 'reportesMongo' or \
            obj2._meta.app_label == 'reportesMongo':
            return True
        return None
        
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the reportesMongo app only appears in the 'mongo_db'
        database.
        """
        if app_label == 'reportesMongo':
            return db == 'mongo_db'
        return None