#include <libtorrent/session.hpp>
#include <libtorrent/add_torrent_params.hpp>
#include <libtorrent/torrent_handle.hpp>
#include <libtorrent/magnet_uri.hpp>

#include <boost/asio.hpp>
#include <libtorrent/session.hpp>
#include <libtorrent/torrent_status.hpp>
#include <libtorrent/entry.hpp>
#include <libtorrent/alert_types.hpp>
#include <libtorrent/bencode.hpp>
#include <libtorrent/torrent_handle.hpp>
#include <libtorrent/magnet_uri.hpp>
#include <libtorrent/alert_types.hpp>
#include <libtorrent/alert.hpp>
#include <iostream>

int main() {
    boost::asio::io_service io_service;
    libtorrent::session session(io_service, "libtorrent_session");

    libtorrent::add_torrent_params params;
    params.url = "magnet:?xt=urn:btih:0a7bdf58622d4b46f4f3ff992a15a4b36e8dc710&dn=%5BYoghurt%5D%20Tokyo%20Ghoul%20OVA%20%28Jack%20%2B%20Pinto%29%20%5BBD%201080p%20AVC%20FLAC%5D&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce";
    libtorrent::torrent_handle handle = session.add_torrent(params);

    session.start_dht();
    session.start_upnp();
    session.start_natp();

    while (true) {
        io_service.run();

        libtorrent::torrent_status status = handle.status();

        std::cout << "Progress: " << status.progress * 100 << "%\n";
        std::cout << "Download rate: " << status.download_rate / 1024 / 1024 << " MB/s\n";
        std::cout << "Upload rate: " << status.upload_rate / 1024 / 1024 << " MB/s\n";

        if (status.is_finished()) {
            std::cout << "Download completed!\n";
            break;
        }
    }

    return 0;
}