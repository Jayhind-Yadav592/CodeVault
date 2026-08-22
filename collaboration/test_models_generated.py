from django.test import TestCase
from django.utils import timezone
from .models import *

class OrganizationMemberModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = OrganizationMember._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = OrganizationMember._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = OrganizationMember._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = OrganizationMember._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = OrganizationMember._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = OrganizationMember._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_organization(self):
        field = OrganizationMember._meta.get_field('organization')
        self.assertIsNotNone(field)
    def test_field_type_organization(self):
        field = OrganizationMember._meta.get_field('organization')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_user(self):
        field = OrganizationMember._meta.get_field('user')
        self.assertIsNotNone(field)
    def test_field_type_user(self):
        field = OrganizationMember._meta.get_field('user')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_role(self):
        field = OrganizationMember._meta.get_field('role')
        self.assertIsNotNone(field)
    def test_field_type_role(self):
        field = OrganizationMember._meta.get_field('role')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_status(self):
        field = OrganizationMember._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = OrganizationMember._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_joined_date(self):
        field = OrganizationMember._meta.get_field('joined_date')
        self.assertIsNotNone(field)
    def test_field_type_joined_date(self):
        field = OrganizationMember._meta.get_field('joined_date')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_invited_by(self):
        field = OrganizationMember._meta.get_field('invited_by')
        self.assertIsNotNone(field)
    def test_field_type_invited_by(self):
        field = OrganizationMember._meta.get_field('invited_by')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_last_activity(self):
        field = OrganizationMember._meta.get_field('last_activity')
        self.assertIsNotNone(field)
    def test_field_type_last_activity(self):
        field = OrganizationMember._meta.get_field('last_activity')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')

class OrganizationInvitationModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = OrganizationInvitation._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = OrganizationInvitation._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = OrganizationInvitation._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = OrganizationInvitation._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = OrganizationInvitation._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = OrganizationInvitation._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_organization(self):
        field = OrganizationInvitation._meta.get_field('organization')
        self.assertIsNotNone(field)
    def test_field_type_organization(self):
        field = OrganizationInvitation._meta.get_field('organization')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_email(self):
        field = OrganizationInvitation._meta.get_field('email')
        self.assertIsNotNone(field)
    def test_field_type_email(self):
        field = OrganizationInvitation._meta.get_field('email')
        self.assertEqual(field.__class__.__name__, 'EmailField')
    def test_field_existence_role(self):
        field = OrganizationInvitation._meta.get_field('role')
        self.assertIsNotNone(field)
    def test_field_type_role(self):
        field = OrganizationInvitation._meta.get_field('role')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_inviter(self):
        field = OrganizationInvitation._meta.get_field('inviter')
        self.assertIsNotNone(field)
    def test_field_type_inviter(self):
        field = OrganizationInvitation._meta.get_field('inviter')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_status(self):
        field = OrganizationInvitation._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = OrganizationInvitation._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_token_hash(self):
        field = OrganizationInvitation._meta.get_field('token_hash')
        self.assertIsNotNone(field)
    def test_field_type_token_hash(self):
        field = OrganizationInvitation._meta.get_field('token_hash')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_expires_at(self):
        field = OrganizationInvitation._meta.get_field('expires_at')
        self.assertIsNotNone(field)
    def test_field_type_expires_at(self):
        field = OrganizationInvitation._meta.get_field('expires_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')

class ProjectTeamMemberModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ProjectTeamMember._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ProjectTeamMember._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ProjectTeamMember._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ProjectTeamMember._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ProjectTeamMember._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ProjectTeamMember._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = ProjectTeamMember._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = ProjectTeamMember._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_user(self):
        field = ProjectTeamMember._meta.get_field('user')
        self.assertIsNotNone(field)
    def test_field_type_user(self):
        field = ProjectTeamMember._meta.get_field('user')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_role(self):
        field = ProjectTeamMember._meta.get_field('role')
        self.assertIsNotNone(field)
    def test_field_type_role(self):
        field = ProjectTeamMember._meta.get_field('role')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_status(self):
        field = ProjectTeamMember._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = ProjectTeamMember._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_joined_date(self):
        field = ProjectTeamMember._meta.get_field('joined_date')
        self.assertIsNotNone(field)
    def test_field_type_joined_date(self):
        field = ProjectTeamMember._meta.get_field('joined_date')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_last_activity(self):
        field = ProjectTeamMember._meta.get_field('last_activity')
        self.assertIsNotNone(field)
    def test_field_type_last_activity(self):
        field = ProjectTeamMember._meta.get_field('last_activity')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')

class ProjectMilestoneModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ProjectMilestone._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ProjectMilestone._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ProjectMilestone._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ProjectMilestone._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ProjectMilestone._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ProjectMilestone._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = ProjectMilestone._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = ProjectMilestone._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_name(self):
        field = ProjectMilestone._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = ProjectMilestone._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = ProjectMilestone._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = ProjectMilestone._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_start_date(self):
        field = ProjectMilestone._meta.get_field('start_date')
        self.assertIsNotNone(field)
    def test_field_type_start_date(self):
        field = ProjectMilestone._meta.get_field('start_date')
        self.assertEqual(field.__class__.__name__, 'DateField')
    def test_field_existence_target_date(self):
        field = ProjectMilestone._meta.get_field('target_date')
        self.assertIsNotNone(field)
    def test_field_type_target_date(self):
        field = ProjectMilestone._meta.get_field('target_date')
        self.assertEqual(field.__class__.__name__, 'DateField')
    def test_field_existence_status(self):
        field = ProjectMilestone._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = ProjectMilestone._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_completion_percentage(self):
        field = ProjectMilestone._meta.get_field('completion_percentage')
        self.assertIsNotNone(field)
    def test_field_type_completion_percentage(self):
        field = ProjectMilestone._meta.get_field('completion_percentage')
        self.assertEqual(field.__class__.__name__, 'IntegerField')

class ProjectTaskModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ProjectTask._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ProjectTask._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ProjectTask._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ProjectTask._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ProjectTask._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ProjectTask._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = ProjectTask._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = ProjectTask._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_milestone(self):
        field = ProjectTask._meta.get_field('milestone')
        self.assertIsNotNone(field)
    def test_field_type_milestone(self):
        field = ProjectTask._meta.get_field('milestone')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_title(self):
        field = ProjectTask._meta.get_field('title')
        self.assertIsNotNone(field)
    def test_field_type_title(self):
        field = ProjectTask._meta.get_field('title')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = ProjectTask._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = ProjectTask._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_assignee(self):
        field = ProjectTask._meta.get_field('assignee')
        self.assertIsNotNone(field)
    def test_field_type_assignee(self):
        field = ProjectTask._meta.get_field('assignee')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_reporter(self):
        field = ProjectTask._meta.get_field('reporter')
        self.assertIsNotNone(field)
    def test_field_type_reporter(self):
        field = ProjectTask._meta.get_field('reporter')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_status(self):
        field = ProjectTask._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = ProjectTask._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_priority(self):
        field = ProjectTask._meta.get_field('priority')
        self.assertIsNotNone(field)
    def test_field_type_priority(self):
        field = ProjectTask._meta.get_field('priority')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_due_date(self):
        field = ProjectTask._meta.get_field('due_date')
        self.assertIsNotNone(field)
    def test_field_type_due_date(self):
        field = ProjectTask._meta.get_field('due_date')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_labels(self):
        field = ProjectTask._meta.get_field('labels')
        self.assertIsNotNone(field)
    def test_field_type_labels(self):
        field = ProjectTask._meta.get_field('labels')
        self.assertEqual(field.__class__.__name__, 'JSONField')

class TaskCommentModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = TaskComment._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = TaskComment._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = TaskComment._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = TaskComment._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = TaskComment._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = TaskComment._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_task(self):
        field = TaskComment._meta.get_field('task')
        self.assertIsNotNone(field)
    def test_field_type_task(self):
        field = TaskComment._meta.get_field('task')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_author(self):
        field = TaskComment._meta.get_field('author')
        self.assertIsNotNone(field)
    def test_field_type_author(self):
        field = TaskComment._meta.get_field('author')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_body(self):
        field = TaskComment._meta.get_field('body')
        self.assertIsNotNone(field)
    def test_field_type_body(self):
        field = TaskComment._meta.get_field('body')
        self.assertEqual(field.__class__.__name__, 'TextField')

class ProjectDiscussionModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ProjectDiscussion._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ProjectDiscussion._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ProjectDiscussion._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ProjectDiscussion._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ProjectDiscussion._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ProjectDiscussion._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = ProjectDiscussion._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = ProjectDiscussion._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_title(self):
        field = ProjectDiscussion._meta.get_field('title')
        self.assertIsNotNone(field)
    def test_field_type_title(self):
        field = ProjectDiscussion._meta.get_field('title')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_body(self):
        field = ProjectDiscussion._meta.get_field('body')
        self.assertIsNotNone(field)
    def test_field_type_body(self):
        field = ProjectDiscussion._meta.get_field('body')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_author(self):
        field = ProjectDiscussion._meta.get_field('author')
        self.assertIsNotNone(field)
    def test_field_type_author(self):
        field = ProjectDiscussion._meta.get_field('author')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_category(self):
        field = ProjectDiscussion._meta.get_field('category')
        self.assertIsNotNone(field)
    def test_field_type_category(self):
        field = ProjectDiscussion._meta.get_field('category')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_status(self):
        field = ProjectDiscussion._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = ProjectDiscussion._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')

class DiscussionCommentModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = DiscussionComment._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = DiscussionComment._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = DiscussionComment._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = DiscussionComment._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = DiscussionComment._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = DiscussionComment._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_discussion(self):
        field = DiscussionComment._meta.get_field('discussion')
        self.assertIsNotNone(field)
    def test_field_type_discussion(self):
        field = DiscussionComment._meta.get_field('discussion')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_author(self):
        field = DiscussionComment._meta.get_field('author')
        self.assertIsNotNone(field)
    def test_field_type_author(self):
        field = DiscussionComment._meta.get_field('author')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_body(self):
        field = DiscussionComment._meta.get_field('body')
        self.assertIsNotNone(field)
    def test_field_type_body(self):
        field = DiscussionComment._meta.get_field('body')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_is_resolution(self):
        field = DiscussionComment._meta.get_field('is_resolution')
        self.assertIsNotNone(field)
    def test_field_type_is_resolution(self):
        field = DiscussionComment._meta.get_field('is_resolution')
        self.assertEqual(field.__class__.__name__, 'BooleanField')

class ArchitectureDecisionRecordModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ArchitectureDecisionRecord._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ArchitectureDecisionRecord._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ArchitectureDecisionRecord._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ArchitectureDecisionRecord._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ArchitectureDecisionRecord._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ArchitectureDecisionRecord._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = ArchitectureDecisionRecord._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = ArchitectureDecisionRecord._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_title(self):
        field = ArchitectureDecisionRecord._meta.get_field('title')
        self.assertIsNotNone(field)
    def test_field_type_title(self):
        field = ArchitectureDecisionRecord._meta.get_field('title')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_context(self):
        field = ArchitectureDecisionRecord._meta.get_field('context')
        self.assertIsNotNone(field)
    def test_field_type_context(self):
        field = ArchitectureDecisionRecord._meta.get_field('context')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_decision(self):
        field = ArchitectureDecisionRecord._meta.get_field('decision')
        self.assertIsNotNone(field)
    def test_field_type_decision(self):
        field = ArchitectureDecisionRecord._meta.get_field('decision')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_alternatives(self):
        field = ArchitectureDecisionRecord._meta.get_field('alternatives')
        self.assertIsNotNone(field)
    def test_field_type_alternatives(self):
        field = ArchitectureDecisionRecord._meta.get_field('alternatives')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_consequences(self):
        field = ArchitectureDecisionRecord._meta.get_field('consequences')
        self.assertIsNotNone(field)
    def test_field_type_consequences(self):
        field = ArchitectureDecisionRecord._meta.get_field('consequences')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_author(self):
        field = ArchitectureDecisionRecord._meta.get_field('author')
        self.assertIsNotNone(field)
    def test_field_type_author(self):
        field = ArchitectureDecisionRecord._meta.get_field('author')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_status(self):
        field = ArchitectureDecisionRecord._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = ArchitectureDecisionRecord._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_date_logged(self):
        field = ArchitectureDecisionRecord._meta.get_field('date_logged')
        self.assertIsNotNone(field)
    def test_field_type_date_logged(self):
        field = ArchitectureDecisionRecord._meta.get_field('date_logged')
        self.assertEqual(field.__class__.__name__, 'DateField')

class ProjectReleaseModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ProjectRelease._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ProjectRelease._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ProjectRelease._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ProjectRelease._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ProjectRelease._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ProjectRelease._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = ProjectRelease._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = ProjectRelease._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_snapshot(self):
        field = ProjectRelease._meta.get_field('snapshot')
        self.assertIsNotNone(field)
    def test_field_type_snapshot(self):
        field = ProjectRelease._meta.get_field('snapshot')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_version(self):
        field = ProjectRelease._meta.get_field('version')
        self.assertIsNotNone(field)
    def test_field_type_version(self):
        field = ProjectRelease._meta.get_field('version')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_release_title(self):
        field = ProjectRelease._meta.get_field('release_title')
        self.assertIsNotNone(field)
    def test_field_type_release_title(self):
        field = ProjectRelease._meta.get_field('release_title')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_release_notes(self):
        field = ProjectRelease._meta.get_field('release_notes')
        self.assertIsNotNone(field)
    def test_field_type_release_notes(self):
        field = ProjectRelease._meta.get_field('release_notes')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_release_date(self):
        field = ProjectRelease._meta.get_field('release_date')
        self.assertIsNotNone(field)
    def test_field_type_release_date(self):
        field = ProjectRelease._meta.get_field('release_date')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_status(self):
        field = ProjectRelease._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = ProjectRelease._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')

class ActivityEventModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ActivityEvent._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ActivityEvent._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ActivityEvent._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ActivityEvent._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ActivityEvent._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ActivityEvent._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = ActivityEvent._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = ActivityEvent._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_actor(self):
        field = ActivityEvent._meta.get_field('actor')
        self.assertIsNotNone(field)
    def test_field_type_actor(self):
        field = ActivityEvent._meta.get_field('actor')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_event_type(self):
        field = ActivityEvent._meta.get_field('event_type')
        self.assertIsNotNone(field)
    def test_field_type_event_type(self):
        field = ActivityEvent._meta.get_field('event_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = ActivityEvent._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = ActivityEvent._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_metadata(self):
        field = ActivityEvent._meta.get_field('metadata')
        self.assertIsNotNone(field)
    def test_field_type_metadata(self):
        field = ActivityEvent._meta.get_field('metadata')
        self.assertEqual(field.__class__.__name__, 'JSONField')


