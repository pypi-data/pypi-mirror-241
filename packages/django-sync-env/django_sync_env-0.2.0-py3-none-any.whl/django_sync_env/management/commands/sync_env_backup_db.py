"""
Command for backup database.
"""
import logging

from django.core.management.base import CommandError
import os
from django_sync_env import settings, utils
from django_sync_env.db.base import get_connector
from django_sync_env.storage import StorageError, get_storage
from django_sync_env.management.commands._base import BaseSyncBackupCommand, make_option


class Command(BaseSyncBackupCommand):
    help = "Backup a database, encrypt and/or compress and write to " "storage." ""
    content_type = "db"
    logger = logging.getLogger("sync_env")

    option_list = BaseSyncBackupCommand.option_list + (
        # TODO enable the option to specify particular databases
        # make_option(
        #     "-d",
        #     "--database",
        #     help="Database(s) to backup specified by key separated by commas(default: all)",
        # ),
        # TODO enable the option to exclude particular tables in particular databases
        # make_option(
        #     "-x", "--exclude-tables",
        #     default=None,
        #     help="Exclude tables from backup",
        # ),
    )

    @utils.email_uncaught_exception
    def handle(self, **options):
        self._set_logger_level()

        self.verbosity = options.get("verbosity")
        self.quiet = options.get("quiet")
        self.compress = True  # enforce compression
        self.exclude_tables = None  # not in use yet
        # self.exclude_tables = options.get("exclude_tables")  # wip for later release

        database_keys = settings.DATABASES
        storage_config = utils.get_storage_config(settings.ENVIRONMENT, settings.SYNC_ENV_ENVIRONMENTS)
        storage = get_storage(settings.ENVIRONMENT, storage_config)

        for database_key in database_keys:
            self.connector = get_connector(database_key)
            if self.connector and self.exclude_tables:
                self.connector.exclude.extend(
                    list(self.exclude_tables.replace(" ", "").split(","))
                )
            database = self.connector.settings

            try:
                self._save_new_backup(database, storage)
            except StorageError as err:
                raise CommandError(err) from err

            self.logger.info(f"Successfully backed up database: {database['NAME']}!", )

    def _save_new_backup(self, database, storage):
        """
        Save a new backup file.
        """
        self.logger.info("Backing Up Database: %s", database["NAME"])
        # Get backup and name
        outputfile = self.connector.create_dump()

        filename = self.connector.generate_filename(
            environment=settings.ENVIRONMENT,
            database_name=database["NAME"]
        )

        if self.compress:
            compressed_file, filename = utils.compress_file(outputfile, filename)
            outputfile = compressed_file

        self.logger.info("Backup size: %s", utils.handle_size(outputfile))
        # Store backup
        outputfile.seek(0)

        if storage.name == 'FileSystemStorage':
            file_path_out = os.path.join(storage.storage._location, filename)
            self.write_local_file(outputfile, file_path_out)
        else:
            self.write_to_storage(storage, outputfile, filename)
