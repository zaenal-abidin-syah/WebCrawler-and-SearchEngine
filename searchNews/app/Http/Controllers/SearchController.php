<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;

class SearchController extends Controller
{
    public function index()
    {
        return view('search');
    }

    public function search(Request $request)
    {
        $query = $request->get('query');
        $rank = $request->get('rank');
        // return view('search', $data);
        // echo $query;
        $process = Process::run("python3 query.py newsdb {$rank} '{$query}'");

        if (!$process->successful()) {
            // Proses berhasil dijalankan
            // $output = $process->getOutput();
            // throw new ProcessFailedException($process);
            return response()->json(['error' => $process->output()]);
            // return response()->json();
            // Lakukan sesuatu dengan output
        }

        $list_data = array_filter(explode("\n", $process->output()));
        // return response()->json($list_data);


        $data = array();

        // foreach ($list_data as $book) {
        //     $dataj =  json_decode($book, true);
        //     array_push($data, '<div class="card p-2 mb-4 mx-3 col-sm-3" style="width: 14rem;">
        //     <img src="'. $dataj['img'] .'" class="card-img-top" alt="'. $dataj['judul'] . '">
        //     <div class="card-body">
        //         <h6 class="card-title">'. $dataj['judul'] . '</h6>
        //         <p class="card-text">'. implode(',', $dataj['genre']) . '</p>
        //         </div>
        //         <a href="#" class="btn btn-primary"data-bs-toggle="modal" data-bs-target="#anime">More</a>
        // </div>
        // ');
        // }
        // return response()->json($data);
        foreach ($list_data as $news) {
            $dataj =  json_decode($news, true);
            array_push($data, $dataj);
        }
        $data['data'] = $data;
        return view('search', $data);

        // return response()->json($data);
    }
}
