from rest_framework import serializers

from snippets.models import STYLE_CHOICES, Snippet


class SnippetSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(
    #     view_name='snippet-highlight',
    #     format= 'html'
    # )
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style',
                  # 'highlight', 'owner', 'url',
                  )