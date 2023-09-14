 File "/home/user103/Desktop/website_performance_metrics--lighthouse/seo_tool/manage.py", line 22, in <module>
    main()
  File "/home/user103/Desktop/website_performance_metrics--lighthouse/seo_tool/manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/usr/lib/python3/dist-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "/usr/lib/python3/dist-packages/django/core/management/__init__.py", line 413, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/usr/lib/python3/dist-packages/django/core/management/base.py", line 354, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/usr/lib/python3/dist-packages/django/core/management/base.py", line 398, in execute
    output = self.handle(*args, **options)
  File "/usr/lib/python3/dist-packages/django/core/management/base.py", line 89, in wrapped
    res = handle_func(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/django/core/management/commands/migrate.py", line 244, in handle
    post_migrate_state = executor.migrate(
  File "/usr/lib/python3/dist-packages/django/db/migrations/executor.py", line 117, in migrate
    state = self._migrate_all_forwards(state, plan, full_plan, fake=fake, fake_initial=fake_initial)
  File "/usr/lib/python3/dist-packages/django/db/migrations/executor.py", line 147, in _migrate_all_forwards
    state = self.apply_migration(state, migration, fake=fake, fake_initial=fake_initial)
  File "/usr/lib/python3/dist-packages/django/db/migrations/executor.py", line 227, in apply_migration
    state = migration.apply(state, schema_editor)
  File "/usr/lib/python3/dist-packages/django/db/migrations/migration.py", line 126, in apply
    operation.database_forwards(self.app_label, schema_editor, old_state, project_state)
  File "/usr/lib/python3/dist-packages/django/db/migrations/operations/fields.py", line 104, in database_forwards
    schema_editor.add_field(
  File "/usr/lib/python3/dist-packages/django/db/backends/base/schema.py", line 490, in add_field
    definition, params = self.column_sql(model, field, include_default=True)
  File "/usr/lib/python3/dist-packages/django/db/backends/base/schema.py", line 237, in column_sql
    default_value = self.effective_default(field)
  File "/usr/lib/python3/dist-packages/django/db/backends/base/schema.py", line 324, in effective_default
    return field.get_db_prep_save(self._effective_default(field), self.connection)
  File "/usr/lib/python3/dist-packages/django/db/models/fields/__init__.py", line 842, in get_db_prep_save
    return self.get_db_prep_value(value, connection=connection, prepared=False)
  File "/usr/lib/python3/dist-packages/django/db/models/fields/__init__.py", line 1427, in get_db_prep_value
    value = self.get_prep_value(value)
  File "/usr/lib/python3/dist-packages/django/db/models/fields/__init__.py", line 1406, in get_prep_value
    value = super().get_prep_value(value)
  File "/usr/lib/python3/dist-packages/django/db/models/fields/__init__.py", line 1266, in get_prep_value
    return self.to_python(value)
  File "/usr/lib/python3/dist-packages/django/db/models/fields/__init__.py", line 1367, in to_python
    parsed = parse_datetime(value)
  File "/usr/lib/python3/dist-packages/django/utils/dateparse.py", line 107, in parse_datetime
    match = datetime_re.match(value)
TypeError: expected string or bytes-like object
