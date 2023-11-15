# Import python functionality:
import os

# Import Django functionality
from django.test import TestCase, tag
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

# Import Django-models from this app:
from .models import fontregion as db_fontregion
from .models import lineregion as db_lineregion
from .models import readingline as db_readingline
from .models import readinghistogram as db_readinghistogram
from .models import textpart as db_textpart
from .models import title as db_title
from .models import body as db_body
from .models import footer as db_footer
from .models import headlines as db_headlines
from .models import headlines_hierarchy as db_headlines_hierarchy
from .models import enumeration as db_enumeration
from .models import enumeration_hierarchy as db_enumeration_hierarchy
from .models import textalinea as db_textalinea
from .models import textsplitter as db_textsplitter
from .models import Native_TOC_Element as db_Native_TOC_Element
from .models import breakdown_decisions as db_breakdown_decisions

# Creation of the test classes:
@tag("database", "unit", "admin")
class Analyze_admin_Tests(TestCase):
    """
    Note: Always inherit from TestCase, so that we can use a test-database.
    This class will contain the tests for the log_newtask of the analysis-app.
    """

    @classmethod
    def setUpTestData(self):
        """
        This function will set up a test document in the database, so multiple tests
        can actually use it.
        """

        # Put in some models:
        db_textpart_inst = db_textpart()
        db_textpart_inst.save()

        db_fontregion_inst = db_fontregion()
        db_fontregion_inst.textpart = db_textpart_inst
        db_fontregion_inst.save()

        db_lineregion_inst = db_lineregion()
        db_lineregion_inst.textpart = db_textpart_inst
        db_lineregion_inst.save()

        db_readingline_inst = db_readingline()
        db_readingline_inst.textpart = db_textpart_inst
        db_readingline_inst.save()

        db_readinghistogram_inst = db_readinghistogram()
        db_readinghistogram_inst.textpart = db_textpart_inst
        db_readinghistogram_inst.save()

        db_title_inst = db_title()
        db_title_inst.textpart = db_textpart_inst
        db_title_inst.save()

        db_body_inst = db_body()
        db_body_inst.textpart = db_textpart_inst
        db_body_inst.save()

        db_footer_inst = db_footer()
        db_footer_inst.textpart = db_textpart_inst
        db_footer_inst.save()

        db_headlines_inst = db_headlines()
        db_headlines_inst.textpart = db_textpart_inst
        db_headlines_inst.save()

        db_enumeration_inst = db_enumeration()
        db_enumeration_inst.textpart = db_textpart_inst
        db_enumeration_inst.save()

        db_headlines_hierarchy_inst = db_headlines_hierarchy()
        db_headlines_hierarchy_inst.headlines = db_headlines_inst
        db_headlines_hierarchy_inst.save()

        db_enumeration_hierarchy_inst = db_enumeration_hierarchy()
        db_enumeration_hierarchy_inst.enumeration = db_enumeration_inst
        db_enumeration_hierarchy_inst.save()

        db_textsplitter_inst = db_textsplitter()
        db_textsplitter_inst.title = db_title_inst
        db_textsplitter_inst.body = db_body_inst
        db_textsplitter_inst.footer = db_footer_inst
        db_textsplitter_inst.headlines = db_headlines_inst
        db_textsplitter_inst.enumeration = db_enumeration_inst
        db_textsplitter_inst.textpart = db_textpart_inst
        db_textsplitter_inst.save()

        db_Native_TOC_Element_inst = db_Native_TOC_Element()
        db_Native_TOC_Element_inst.textsplitter = db_textsplitter_inst
        db_Native_TOC_Element_inst.save()

        db_breakdown_decisions_inst = db_breakdown_decisions()
        db_breakdown_decisions_inst.textsplitter = db_textsplitter_inst
        db_breakdown_decisions_inst.save()

        db_textalinea_inst = db_textalinea()
        db_textalinea_inst.textsplitter = db_textsplitter_inst
        db_textalinea_inst.textpart = db_textpart_inst
        db_textalinea_inst.save()

        # Obtain some permissions:
        content_type = ContentType.objects.get_for_model(db_textsplitter)
        permissions = Permission.objects.filter(content_type=content_type)

        # Collect permissions:
        view_perm = ""
        for perm in permissions:
            if "view" in str(perm):
                view_perm = perm
        add_perm = ""
        for perm in permissions:
            if "add" in str(perm):
                add_perm = perm
        change_perm = ""
        for perm in permissions:
            if "change" in str(perm):
                change_perm = perm
        delete_perm = ""
        for perm in permissions:
            if "delete" in str(perm):
                delete_perm = perm

        # Create test users:
        self.test_user1 = User.objects.create_user(
            username="MrBeanUser", password="TeddyUser", email="mrbeanuser@teddy.com"
        )
        self.test_user1.is_staff = False
        self.test_user1.is_superuser = False
        self.test_user1.user_permissions.add(view_perm)
        self.test_user1.user_permissions.add(change_perm)
        self.test_user1.user_permissions.add(delete_perm)
        self.test_user1.user_permissions.add(add_perm)
        self.test_user1.save()

        self.test_user2 = User.objects.create_user(
            username="MrBeanStaff", password="TeddyStaff", email="mrbeanstaff@teddy.com"
        )
        self.test_user2.is_staff = True
        self.test_user2.is_superuser = False
        self.test_user2.user_permissions.add(view_perm)
        self.test_user2.user_permissions.add(change_perm)
        self.test_user2.user_permissions.add(delete_perm)
        self.test_user2.user_permissions.add(add_perm)
        self.test_user2.save()

        self.test_user3 = User.objects.create_user(
            username="MrBeanSuperuser", password="TeddySuperuser", email="mrbeansuperuser@teddy.com"
        )
        self.test_user3.is_staff = True
        self.test_user3.is_superuser = True
        self.test_user3.user_permissions.add(view_perm)
        self.test_user3.user_permissions.add(change_perm)
        self.test_user3.user_permissions.add(add_perm)
        self.test_user3.user_permissions.add(delete_perm)
        self.test_user3.save()

    def test_custom_admin_1(self):
        """
        Unit test for test_log_newtask (to create a new pending task in the que):
        # Parameters: none; # Returns (bool): succes of the text.
        # Author: Christiaan Douma
        """

        # Log the test user in & request the url & view by django client:
        self.client.login(username="MrBeanUser", password="TeddyUser")
        response = self.client.get("/admin/djangotextsplitter/textsplitter/add/")
        self.assertEqual(response.status_code, 302)

    def test_custom_admin_2(self):
        """
        Unit test for test_log_newtask (to create a new pending task in the que):
        # Parameters: none; # Returns (bool): succes of the text.
        # Author: Christiaan Douma
        """

        # Log the test user in & request the url & view by django client:
        self.client.login(username="MrBeanStaff", password="TeddyStaff")
        response = self.client.get("/admin/djangotextsplitter/textsplitter/add/")
        self.assertEqual(response.status_code, 200)

    def test_custom_admin_3(self):
        """
        Unit test for test_log_newtask (to create a new pending task in the que):
        # Parameters: none; # Returns (bool): succes of the text.
        # Author: Christiaan Douma
        """

        # Log the test user in & request the url & view by django client:
        self.client.login(username="MrBeanSuperuser", password="TeddySuperuser")
        response = self.client.get("/admin/djangotextsplitter/textsplitter/add/")
        self.assertEqual(response.status_code, 200)
