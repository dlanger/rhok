// Generated by CoffeeScript 1.3.1
(function() {
  var App, Forms,
    __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  Forms = RHOK.module('forms');

  App = (function() {

    App.name = 'App';

    function App() {
      this.init = __bind(this.init, this);

    }

    App.prototype.$el = $('#Main');

    App.prototype.init = function() {
      this.fieldsets = new Backbone.Collection();
      this.fieldsets.add(new Forms.Tombstone({
        header: 'Personal Information'
      }));
      this.fieldsets.add(new Forms.Learning({
        header: 'Learning'
      }));
      this.fieldsets.add(new Forms.Adaptive({
        header: 'Adaptive'
      }));
      this.fieldsets.add(new Forms.FineMotorSkills({
        header: 'Fine Motor Skills'
      }));
      this.fieldsets.add(new Forms.GrossMotorSkills({
        header: 'Gross Motor Skills'
      }));
      this.formView = new Forms.FormView({
        collection: this.fieldsets
      }).render();
      return this.$el.append(this.formView.el);
    };

    return App;

  })();

  window.app = new App();

  $(window.app.init);

}).call(this);
