<?php

use App\Http\Controllers\SearchController;
use Illuminate\Support\Facades\Route;



// Route::get('/', function () {
//     return view('welcome');
// });

// Route::get('/search', );

Route::get('/', [SearchController::class, 'index']);
Route::get('/search', [SearchController::class, 'search']);
