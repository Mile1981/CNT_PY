/*=========================================================================================
    File Name: picker-date-time.js
    Description: Pick a date/time Picker, Date Range Picker JS
    ----------------------------------------------------------------------------------------
    Item Name: Apex - Responsive Admin Theme
    Version: 2.1
    Author: Pixinvent
    Author URL: hhttp://www.themeforest.net/user/pixinvent
==========================================================================================*/
(function(window, document, $) {
	'use strict';


	
	// Disable weekday range
function calendario_medico(){
	console.log(dias_medico);

}

	

	// Basic time
	$('.pickatime').pickatime();

	// Hide Button
	$('.pickatime-button').pickatime({
		clear: '',
	});

	// Format options
	$('.pickatime-format').pickatime({
		// Escape any “rule” characters with an exclamation mark (!).
		format: 'T!ime selected: h:i a',
		formatLabel: 'h:i a',
		formatSubmit: 'HH:i',
		hiddenPrefix: 'prefix__',
		hiddenSuffix: '__suffix'
	});

	// Format options
	$('.pickatime-formatTime').pickatime({
		// Escape any “rule” characters with an exclamation mark (!).
		format: 'T!ime selected: h:i a',
		formatLabel: '<b>h</b>:i <!i>a</!i>',
		formatSubmit: 'HH:i',
		hiddenPrefix: 'prefix__',
		hiddenSuffix: '__suffix'
	});

	// Format options
	$('.pickatime-formatlabel').pickatime({
		formatLabel: function(time) {
			var hours = ( time.pick - this.get('now').pick ) / 60,
				label = hours < 0 ? ' !hours to now' : hours > 0 ? ' !hours from now' : 'now';
			return  'h:i a <sm!all>' + ( hours ? Math.abs(hours) : '' ) + label +'</sm!all>';
		}
	});

	// Date range to select
	$( '.pickatime-minmax' ).pickatime({

		// Using Javascript
		min: new Date(2015,3,20,7),
		max: new Date(2015,7,14,18,30)

		// Using Array
		/*min: [7,30],
		max: [14,0]*/
	});

	// Time using Integer & Boolean
	$('.pickatime-limits').pickatime({
		// An integer (positive/negative) sets it as intervals relative from now.
		min: -5,
		// 'true' sets it to now. 'false' removes any limits.
		max: true
	});

	// Intervals
	$('.pickatime-intervals').pickatime({
		interval: 150
	});

	/*	Diasable Time sets */
	$('.pickatime-disable').pickatime({
		// Disable Using Javascript
		disable: [
			new Date(2016,3,20,4,30),
			new Date(2016,3,20,9)
		]
		// Disable Using Array
		/*disable: [
			[0,30],
			[2,0],
			[8,30],
			[9,0]
		]*/
	});

	// Disable using integers
	$('.pickatime-disable-integer').pickatime({
		disable: [
			3, 5, 7,13,17,21
		]
	});

	// Disable using object
	$('.pickatime-disable-object').pickatime({
		disable: [
			{ from: [2,0], to: [5,30] }
		]
	});

	// Disable All
	$('.pickatime-disable-all').pickatime({
		disable: [
			true,
			3, 5, 7,
			[0,30],
			[2,0],
			[8,30],
			[9,0]
		]
	});

	// Close on a user action
	$('.pickatime-close-action').pickatime({
		closeOnSelect: false,
		closeOnClear: false
	});

	// Events
	$('.pickatime-events').pickatime({
		onStart: function() {
			console.log('This is PickATime!!!');
		},
		onRender: function() {
			console.log('Holla... PickATime Here');
		},
		onOpen: function() {
			console.log('PickATime Opened');
		},
		onClose: function() {
			console.log("I'm Closed now");
		},
		onStop: function() {
			console.log('Have a great day ahead!!');
		},
		onSet: function(context) {
			console.log('All stuff:', context);
		}
	});

	// Picker Translations
	$( '.pickatime-translations' ).pickatime({
		formatSubmit: 'dd/mm/yyyy',
		monthsFull: [ 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre' ],
		monthsShort: [ 'Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Aou', 'Sep', 'Oct', 'Nov', 'Dec' ],
		weekdaysShort: [ 'Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam' ],
		today: 'aujourd\'hui',
		clear: 'clair',
		close: 'Fermer'
	});
})(window, document, jQuery);