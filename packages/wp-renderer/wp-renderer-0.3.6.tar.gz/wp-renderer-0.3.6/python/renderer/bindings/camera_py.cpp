#include <memory>

#include <pybind11/pybind11.h>

#include <renderer/camera/camera_t.hpp>

namespace py = pybind11;

namespace renderer {

// NOLINTNEXTLINE
auto bindings_camera(py::module& m) -> void {
    {
        using Enum = ::renderer::eProjectionType;
        py::enum_<Enum>(m, "ProjectionType")
            .value("PERSPECTIVE", Enum::PERSPECTIVE)
            .value("ORTHOGRAPHIC", Enum::ORTHOGRAPHIC);
    }

    {
        using Class = ::renderer::ProjectionData;
        constexpr auto* ClassName = "ProjectionData";  // NOLINT
        py::class_<Class>(m, ClassName).def(py::init<>());
    }
}

}  // namespace renderer
