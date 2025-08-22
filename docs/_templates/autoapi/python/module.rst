{# Main template - only display if object should be shown #}
{% if obj.display %}

{# Full page layout for own pages #}
{% if is_own_page %}



{{ obj.id }}
{{ "=" * obj.id|length }}

.. py:module:: {{ obj.name }}


{# Module docstring section #}
{% if obj.docstring %}
.. autoapi-nested-parse::

   {{ obj.docstring|indent(3) }}
{% endif %}







{# Submodules block #}
{% block submodules %}
{% set visible_subpackages = obj.subpackages|selectattr("display")|list %}
{% set visible_submodules = obj.submodules|selectattr("display")|list %}
{% set visible_submodules = (visible_subpackages + visible_submodules)|sort %}
{% if visible_submodules %}
Submodules
----------

.. autoapisummary::

  {% for module in visible_submodules %}
   {{ module.id }}
  {% endfor %}


.. gallery::
   :caption: {{ obj.name }}

   {% for module in visible_submodules %}
   {{ module.include_path }}
   {% endfor %}


{% endif %}
{% endblock %}






{% set visible_children = obj.children|selectattr("display")|list %}
{% if visible_children %}






{# Attributes block #}
{% block attributes %}
{% set visible_attributes = visible_children|selectattr("type", "equalto", "data")|list %}
{% if visible_attributes %}
{% if "attribute" in own_page_types or "show-module-summary" in autoapi_options %}

Attributes
----------

{% if "attribute" in own_page_types %}
.. toctree::
   :hidden:

  {% for attribute in visible_attributes %}
   {{ attribute.include_path }}
  {% endfor %}
{% endif %}

.. autoapisummary::

  {% for attribute in visible_attributes %}
   {{ attribute.id }}
  {% endfor %}

{% endif %}
{% endif %}
{% endblock %}






{# Exceptions block #}
{% block exceptions %}
{% set visible_exceptions = visible_children|selectattr("type", "equalto", "exception")|list %}
{% if visible_exceptions %}
{% if "exception" in own_page_types or "show-module-summary" in autoapi_options %}

Exceptions
----------

{% if "exception" in own_page_types %}
.. toctree::
   :hidden:

  {% for exception in visible_exceptions %}
   {{ exception.include_path }}
  {% endfor %}
{% endif %}

.. autoapisummary::

  {% for exception in visible_exceptions %}
   {{ exception.id }}
  {% endfor %}

  
{% endif %}
{% endif %}
{% endblock %}







{# Classes block #}
{% block classes %}
{% set visible_classes = visible_children|selectattr("type", "equalto", "class")|list %}
{% if visible_classes %}
{% if "class" in own_page_types or "show-module-summary" in autoapi_options %}

Classes
-------

{% if "class" in own_page_types %}
.. toctree::
   :hidden:

 {% for klass in visible_classes %}
   {{ klass.include_path }}
 {% endfor %}
{% endif %}

.. autoapisummary::

  {% for klass in visible_classes %}
   {{ klass.id }}
  {% endfor %}


{% endif %}
{% endif %}
{% endblock %}







{# Functions block #}
{% block functions %}
{% set visible_functions = visible_children|selectattr("type", "equalto", "function")|list %}
{% if visible_functions %}
{% if "function" in own_page_types or "show-module-summary" in autoapi_options %}

Functions
---------

{% if "utils" in obj.id %}
.. autosummary::

  {% for function in visible_functions %}
  {{ function.name }}
  {% endfor %}

{% for function in visible_functions %}
.. autoapifunction:: {{ function.name }}
{% endfor %}

{% else %}
.. autoapisummary::

  {% for function in visible_functions %}
   {{ function.id }}
  {% endfor %}



.. base-gallery::
   :caption: {{ obj.name }}

   {% for function in visible_functions %}
   {{ function.name }}
   {% endfor %}
{% endif %}

{% endif %}
{% endif %}
{% endblock %}








{# Additional content that doesn't fit in standard sections #}
{% block additional %}
{% set this_page_children = visible_children|rejectattr("type", "in", own_page_types)|list %}
{% if this_page_children %}
{{ obj.type|title }} Contents
{{ "-" * obj.type|length }}---------

{% for obj_item in this_page_children %}
{{ obj_item.render()|indent(0) }}
{% endfor %}
{% endif %}
{% endblock %}






{% endif %}
{# Simplified layout for embedded modules #}
{% else %}
.. py:module:: {{ obj.name }}

 {% if obj.docstring %}
.. autoapi-nested-parse::

   {{ obj.docstring|indent(6) }}

 {% endif %}
 {% for obj_item in visible_children %}
{{ obj_item.render()|indent(3) }}
 {% endfor %}






{% endif %} {# if is_own_page #}
{% endif %} {# if obj.display #}
