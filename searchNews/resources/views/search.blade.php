<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Search Berita</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">

</head>

<body>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container">
      <a class="navbar-brand" href="#">Search News</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
        </ul>
        <form class="d-flex" role="search" method="get" action="{{ url('/search') }}">
          <input class="form-control me-2" type="search" name="query" placeholder="Search" id="query" aria-label="Search">
          <select class="form-select mx-3" id="rank" name="rank">
            <option value="5">5</option>
            <option value="10">10</option>
            <option value="20">20</option>
          </select>
          <button class="btn btn-primary" type="submit" id="search">Search</button>
        </form>
      </div>
    </div>
  </nav>
  <div class="container mt-5">
    <div class="row content d-flex justify-content-around">
      @isset($data)
        {{-- <p>this is query : {{ $query }}</p> --}}
        
        @foreach ($data as $item)
        <div class="card my-3">
          <h5 class="card-header alert alert-primary">{{$item['kelas']}}</h5>
          <div class="card-body">
            <h5 class="card-title">{{$item['judul']}}</h5>
            <p class="card-text">{{$item['waktu']}}</p>
            <p class="card-text">{{$item['score']}}</p>
            <a href="{{$item['url']}}" class="btn btn-primary">Source</a>
          </div>
        </div>
        @endforeach
        

        {{-- @foreach ($data as $d)
          <p>This is user {{ $data->judul }}</p>
        @endforeach --}}
      @endisset
    </div>
  </div>




  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
  <script src="https://code.jquery.com/jquery-3.6.4.js" integrity="sha256-a9jBBRygX1Bh5lt8GZjXDzyOB+bWve9EiO7tROUtj/E=" crossorigin="anonymous"></script>
  <script src="./script.js"></script>

</body>

</html>