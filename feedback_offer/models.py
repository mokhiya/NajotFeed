from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class OfferModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views_count = models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def count_views(self):
        self.views_count += 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = _('Offers')
        verbose_name = _('Offer')


class ProblemModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    views_count = models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = _('Problems')
        verbose_name = _('Problem')


class ProblemCommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(ProblemModel, null=True, on_delete=models.CASCADE)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['description']
        verbose_name_plural = _('ProblemComments')
        verbose_name = _('ProblemComment')


class OfferCommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(OfferModel, null=True, on_delete=models.CASCADE)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['description']
        verbose_name_plural = _('OfferComments')
        verbose_name = _('OfferComment')


class FAQModel(models.Model):
    question = models.TextField()
    answer = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['question']
        verbose_name_plural = _('FAQs')
        verbose_name = _('FAQ')
