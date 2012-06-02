// Generated by CoffeeScript 1.3.1
(function() {
  var Forms, LEARNING_OPTIONS,
    __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor; child.__super__ = parent.prototype; return child; };

  Forms = RHOK.module('forms');

  LEARNING_OPTIONS = [
    {
      val: 'lt_adequate',
      label: 'Less than adequate'
    }, {
      val: 'adequate',
      label: 'Adequate'
    }, {
      val: 'bt_adequate',
      label: 'Better than adequate'
    }
  ];

  Forms.Learning = (function(_super) {

    __extends(Learning, _super);

    Learning.name = 'Learning';

    function Learning() {
      return Learning.__super__.constructor.apply(this, arguments);
    }

    Learning.prototype.schema = {
      reading: {
        type: 'Radio',
        options: LEARNING_OPTIONS
      },
      spelling: {
        type: 'Radio',
        options: LEARNING_OPTIONS
      },
      math: {
        type: 'Radio',
        options: LEARNING_OPTIONS
      },
      story_writing: {
        title: 'Story Writing',
        type: 'Radio',
        options: LEARNING_OPTIONS
      }
    };

    return Learning;

  })(Backbone.Model);

}).call(this);