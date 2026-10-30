AudioEngine:set_backend("None (Dummy)", "Dummy", "")
local sess = load_session("/home/hatch/workspace/ardour-labwork/FirstTake", "FirstTake")
for r in sess:get_routes():iter() do
  print("route:", r:name())
  local t = r:to_track()
  if t and r:name() == "Tone" then
    print("  processors:", t:nth_processor(0):display_name(), "/", t:nth_processor(1):display_name())
    local pl = t:playlist()
    print("  playlist regions:", pl:region_list():size())
    for reg in pl:region_list():iter() do
      print("  region:", reg:name(), "length:", tostring(reg:length()), "position:", tostring(reg:position()))
    end
  end
end
print("sample rate:", sess:sample_rate(), "nominal tempo check ok")
