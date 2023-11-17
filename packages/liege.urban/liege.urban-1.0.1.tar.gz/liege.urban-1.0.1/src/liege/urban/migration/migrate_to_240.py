# encoding: utf-8

from imio.schedule.config import states_by_status
from imio.schedule.config import STARTED
from imio.schedule.interfaces import TaskConfigNotFound

from Products.urban.interfaces import IUrbanEventType
from Products.urban.interfaces import ILicenceConfig

from plone import api


import logging
import re

logger = logging.getLogger('urban: migrations')


def migrate_env_class_three_tasks(context):
    """ recreate tasks 'recevable', 'irrecevable', ...  for envclassthree """
    logger = logging.getLogger('urban: migrate env class three tasks')
    logger.info("starting migration step")
    catalog = api.portal.get_tool('portal_catalog')
    for task_id in ['TASK_recevable', 'TASK_irrecevable', 'TASK_recevable_avec_conditions']:
        open_task_brains = catalog(portal_type='AutomatedTask', id=task_id, review_state=states_by_status[STARTED])
        for brain in open_task_brains:
            task = brain.getObject()
            try:
                task.get_task_config()
            except TaskConfigNotFound:
                api.content.delete(obj=task)
                logger.info("updated licence {}".format(task.aq_parent.Title()))

    logger.info("migration step done!")


def migrate_default_text_newlines_for_pmws(context):
    """ Delete all new lines from default text of events sent to pm"""
    logger = logging.getLogger('urban: migrate newlines for default texts sent to pm')
    logger.info("starting migration step")
    catalog = api.portal.get_tool('portal_catalog')
    config_brains = catalog(object_provides=[IUrbanEventType.__identifier__, ILicenceConfig.__identifier__])
    for brain in config_brains:
        cfg_obj = brain.getObject()
        if cfg_obj.portal_type == 'LicenceConfig' or cfg_obj.getEventPortalType() in ['UrbanEventCollege', 'UrbanEventMayor', 'UrbanEventNotificationCollege']:
            default_texts = cfg_obj.getTextDefaultValues()
            new_default_texts = []
            for default_text in default_texts:
                new_default_text = default_text.copy()
                new_default_text['text'] = remove_newlines(new_default_text['text'], logger)
                new_default_texts.append(new_default_text)
            cfg_obj.setTextDefaultValues(tuple(new_default_texts))
            logger.info("migrated {} {}".format(cfg_obj.portal_type, cfg_obj))

    logger.info("migration step done!")


def remove_newlines(text, logger):
    if text.find('>&nbsp;</p>') != -1:
        logger.info("migrated text")
        for prefix in ('</p>', ):
            for pre_prefix in ('', '\n', '\n\n', '\r\n', '\r\n\r\n', '\n\r\n\r\n', '\r\n\r\n\r\n'):
                suffixes = [
                    '<p>',
                    '<p style="margin-right:0cm">',
                    '<p style="margin-right:0px">',
                    '<p style="margin-left:0cm">',
                    '<p style="margin-left:0px">',
                    '<p style="text-align:justify">',
                    '<p style="text-align:start">',
                    '<p style="margin-left:0cm; margin-right:0cm">',
                    '<p style="margin-left:0px; margin-right:0px">',
                    '<p style="margin-left:0cm; margin-right:0cm; text-align:justify">',
                    '<p style="margin-left:0cm; margin-right:0cm; text-align:start">',
                    '<p style="margin-left:0px; margin-right:0px; text-align:justify">',
                    '<p style="margin-left:0px; margin-right:0px; text-align:start">'
                ]
                tal_regex = '(<p tal:condition="\w+">)&nbsp;</p>'
                tal_suffixes = re.findall(tal_regex, text)
                for suffix in suffixes + tal_suffixes:
                    to_replace = prefix + pre_prefix + suffix + "&nbsp;</p>"
                    text = text.replace(to_replace, prefix + '\n')
        text = text.replace('<p>&nbsp;</p>', '')
    return text


def migrate(context):
    logger = logging.getLogger('urban: migrate to 2.4')
    logger.info("starting migration steps")
    migrate_env_class_three_tasks(context)
    migrate_default_text_newlines_for_pmws(context)
    logger.info("migration done!")
