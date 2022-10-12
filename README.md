# AGONy



IntegrityError at /AGONy_create_game/1/

NOT NULL constraint failed: AGONy_stage.hero_id

Request Method: 	GET
Request URL: 	http://127.0.0.1:8000/AGONy_create_game/1/
Django Version: 	4.1.2
Exception Type: 	IntegrityError
Exception Value: 	

NOT NULL constraint failed: AGONy_stage.hero_id

Exception Location: 	/home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py, line 357, in execute
Raised during: 	AGONy.views.CreateGameForHero
Python Executable: 	/home/luksi02/gra_rpg/gra_rpg/bin/python3
Python Version: 	3.8.10
Python Path: 	

['/home/luksi02/gra_rpg',
 '/usr/lib/python38.zip',
 '/usr/lib/python3.8',
 '/usr/lib/python3.8/lib-dynload',
 '/home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages']

Server time: 	Wed, 12 Oct 2022 23:07:12 +0000
Traceback Switch to copy-and-paste view

    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/backends/utils.py, line 89, in _execute

                        return self.cursor.execute(sql, params)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py, line 357, in execute

                return Database.Cursor.execute(self, query, params)

         …
    Local vars
    The above exception (NOT NULL constraint failed: AGONy_stage.hero_id) was the direct cause of the following exception:
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/core/handlers/exception.py, line 55, in inner

                        response = get_response(request)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/core/handlers/base.py, line 197, in _get_response

                        response = wrapped_callback(request, *callback_args, **callback_kwargs)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/views/generic/base.py, line 103, in view

                    return self.dispatch(request, *args, **kwargs)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/contrib/auth/mixins.py, line 73, in dispatch

                return super().dispatch(request, *args, **kwargs)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/views/generic/base.py, line 142, in dispatch

                return handler(request, *args, **kwargs)

         …
    Local vars
    /home/luksi02/gra_rpg/AGONy/views.py, line 341, in get

                stage = Stage.objects.create(level=1)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/models/manager.py, line 85, in manager_method

                        return getattr(self.get_queryset(), name)(*args, **kwargs)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/models/query.py, line 671, in create

                obj.save(force_insert=True, using=self.db)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/models/base.py, line 812, in save

                self.save_base(

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/models/base.py, line 863, in save_base

                    updated = self._save_table(

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/models/base.py, line 1006, in _save_table

                    results = self._do_insert(

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/models/base.py, line 1047, in _do_insert

                return manager._insert(

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/models/manager.py, line 85, in manager_method

                        return getattr(self.get_queryset(), name)(*args, **kwargs)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/models/query.py, line 1790, in _insert

                return query.get_compiler(using=using).execute_sql(returning_fields)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/models/sql/compiler.py, line 1660, in execute_sql

                        cursor.execute(sql, params)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/backends/utils.py, line 103, in execute

                    return super().execute(sql, params)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/backends/utils.py, line 67, in execute

                return self._execute_with_wrappers(

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/backends/utils.py, line 80, in _execute_with_wrappers

                return executor(sql, params, many, context)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/backends/utils.py, line 89, in _execute

                        return self.cursor.execute(sql, params)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/utils.py, line 91, in __exit__

                        raise dj_exc_value.with_traceback(traceback) from exc_value

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/backends/utils.py, line 89, in _execute

                        return self.cursor.execute(sql, params)

         …
    Local vars
    /home/luksi02/gra_rpg/gra_rpg/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py, line 357, in execute

                return Database.Cursor.execute(self, query, params)

         …
    Local vars
