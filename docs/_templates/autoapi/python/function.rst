{% if obj.display %}
{% if is_own_page %}
{{ obj.short_name }}
{{ "=" * obj.short_name | length }}

   {% set full_name = obj.id %}
   {% set name_parts = full_name.split('.') %}
   {% if name_parts|length >= 3 and (name_parts[0] == 'stimupy') %}
   {% set category = name_parts[1] %}
   {% set module_name = name_parts[2] %}
   {% set function_name = name_parts[-1] %}
   {% if category in ['components', 'stimuli', 'noises'] %}
   {% set image_path = '/_static/generated_stimuli/' + category + '.' + module_name + '.' + function_name + '.png' %}

   .. image:: {{ image_path }}
      :alt: {{ function_name }} stimulus example
      :align: center
      :width: 400px

{% endif %}
{% endif %}


{% endif %}


.. py:function:: {% if is_own_page %}{{ obj.id }}{% else %}{{ obj.short_name }}{% endif %}({{ obj.args }}){% if obj.return_annotation is not none %} -> {{ obj.return_annotation }}{% endif %}
   {% for (args, return_annotation) in obj.overloads %}

                 {%+ if is_own_page %}{{ obj.id }}{% else %}{{ obj.short_name }}{% endif %}({{ args }}){% if return_annotation is not none %} -> {{ return_annotation }}{% endif %}
   {% endfor %}
   {% for property in obj.properties %}

   :{{ property }}:
   {% endfor %}

   {% if obj.docstring %}


   {{ obj.docstring|indent(3) }}
   {% endif %}




{% endif %} {# if obj.display #}