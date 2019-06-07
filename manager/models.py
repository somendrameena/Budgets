from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User

from .utils import unique_slug_generator


class ExpenseCategory(models.Model):
    name = models.CharField('Name', max_length=255, )
    slug = models.CharField('Slug', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Expense Category'
        verbose_name_plural = 'Expense Categories'

    def __str__(self):
        return self.name


class ExpenseAccount(models.Model):
    name = models.CharField('Name', max_length=255, blank=False)
    slug = models.CharField('Slug', max_length=255, blank=True, null=True)
    balance = models.IntegerField('Balance', blank=True, null=True)

    class Meta:
        verbose_name = 'Expense Account'
        verbose_name_plural = 'Expense Accounts'

    def __str__(self):
        return self.name


class ExpenseItem(models.Model):
    ACCOUNT_CHOICES = (
        ('Cash', "Cash"),
        ('Card', "Card"),
    )
    title = models.CharField('title', max_length=200)
    type = models.ForeignKey(ExpenseCategory, blank=True, null=True, on_delete=models.CASCADE)
    account = models.ForeignKey(ExpenseAccount, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField('date')
    amount = models.IntegerField('amount', default=0)
    description = models.CharField('description', max_length=500, blank=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    added = models.DateTimeField('added on', auto_now_add=True)
    updated = models.DateTimeField('updated', auto_now_add=True)

    def __str__(self):
        return self.title

    def is_free(self):
        return self.amount <= 0

    class Meta:
        verbose_name = 'Expense Item'
        verbose_name_plural = 'Expense Items'


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.updated = timezone.now()
    print("Expense Item updated...")


def ec_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        print("Expense Category updated...")


def ea_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        print("Expense Account updated...")


pre_save.connect(ec_pre_save_receiver, sender=ExpenseCategory)
pre_save.connect(ea_pre_save_receiver, sender=ExpenseAccount)
pre_save.connect(rl_pre_save_receiver, sender=ExpenseItem)
