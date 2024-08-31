function getNews(listNews) {
    let a = "";
    let i = 0;
    console.log(listNews);
    listNews.forEach((news) => {
        //     a += `<div class="card p-2 mb-4 mx-3 col-sm-3" style="width: 14rem;">
        // <img src="${news.img}" class="card-img-top" alt="${news.judul}">
        // <div class="card-body">
        //   <h6 class="card-title">${news.judul}</h6>
        //   <p class="card-text">Genre : ${news.genre.join(",")}</p>
        //   </div>
        //   <button class="btn btn-primary more" data-bs-toggle="modal" data-bs-target="#news" data-id="${i}">More</button>
        // </div>`;

        a += `<div class="card mx-3 my-3" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">${news.judul}</h5>
          <h6 class="card-subtitle mb-2 text-body-secondary">${news.kelas}</h6>
          <p class="card-text">${news.waktu}</p>
          <a href="${news.url}" class="card-link">Card link</a>
        </div>
      </div>`;
        i++;
    });
    return a;
}

$("#search").click(() => {
    let data = [];
    let query = $("#query").val();
    let rank = $("#rank").val();
    console.log("query == ", query);
    console.log("rank == ", rank);
    if (!query || !rank) {
        alert("Masukan Query");
    } else {
        $.ajax({
            url: "/search",
            method: "GET",
            data: {
                query,
                rank,
            },
            dataType: "json",
            success: (data) => {
                console.log(data);
                $(".content").html(getNews(data));

                // i = 0;
                // data.forEach((news) => {
                //     $(`button[data-id=${i}]`).click(function () {
                //         // edit modal
                //         $(".img-nime").attr("src", news.img);
                //         $("#judul").html(news.judul);
                //         $("#genre").html(news.genre.join(","));
                //         $("#rating").html(news.rating);
                //         $("#sinopsis").html(news.sinopsis);
                //         $("#link").attr("href", news.link);
                //     });
                //     i++;
                // });
            },
        });
    }
});
