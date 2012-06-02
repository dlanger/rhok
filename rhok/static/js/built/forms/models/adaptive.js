// Generated by CoffeeScript 1.3.3
(function() {
  var Forms,
    __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  Forms = RHOK.module('forms');

  Forms.Adaptive = (function(_super) {

    __extends(Adaptive, _super);

    function Adaptive() {
      return Adaptive.__super__.constructor.apply(this, arguments);
    }

    Adaptive.prototype.schema = {
      dressing: {
        dataType: 'text',
        validators: ['required'],
        title: 'When did your child begin to dress him/herself?'
      },
      picky_eater: {
        type: 'Select',
        options: [
          {
            val: 'infant',
            label: 'Infant'
          }, {
            val: 'toddler',
            label: 'Toddler'
          }, {
            val: 'child',
            label: 'Child'
          }, {
            val: 'adolescent',
            label: 'Adolescent'
          }, {
            val: 'all',
            label: 'All'
          }
        ],
        title: 'Was your child a picky eater as an'
      },
      sensitve_eater: {
        type: 'Select',
        title: 'Was sensitive to certain textures, smells or colours of food?',
        options: [
          {
            val: 'yes',
            label: 'Yes'
          }, {
            val: 'no',
            label: 'No'
          }
        ]
      },
      difficult_sleeping: {
        type: 'Select',
        title: 'Difficulty falling asleep?',
        options: [
          {
            val: 'yes',
            label: 'Yes'
          }, {
            val: 'no',
            label: 'No'
          }
        ]
      },
      assitence_needed_sleeping: {
        title: 'Does your child request you or another caregiver to be present when falling asleep',
        type: 'Select',
        options: [
          {
            val: 'yes',
            label: 'Yes'
          }, {
            val: 'no',
            label: 'No'
          }
        ]
      },
      sound_sleeping: {
        title: 'Does your child stay asleep through the night?',
        type: 'Radio',
        options: [
          {
            val: 'yes',
            label: 'Yes'
          }, {
            val: 'no',
            label: 'No'
          }
        ]
      },
      toilet_training: {
        title: 'What age was your child toilet trained?'
      }
    };

    return Adaptive;

  })(Backbone.Model);

}).call(this);
